import sys
import json
import os
from utils.pokemon_list_item import PokemonListItem
from data.pokemon_obj import PokemonData
from assets.ui.main_ui import Ui_PokemonSearcher
from assets.ui.clickable_label import ClickableLabel
from PySide6.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QCompleter, QWidget, \
                              QHBoxLayout, QProgressDialog, QLabel, QSizePolicy
from PySide6.QtGui import Qt
from PySide6.QtCore import QStringListModel, QTimer, QEventLoop

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILTERED_POKEDEX_PATH = os.path.join(BASE_DIR, "data/filtered_pokedex.json")
FILTERED_LEARNSET_PATH = os.path.join(BASE_DIR, "data/filtered_learnset.json")

"""TODO:
    Sort by selected stat needs to have a loading wheel
    Implement list widget item click, connect to window / tab with pokemon info
"""

class MainWindow(QMainWindow, Ui_PokemonSearcher):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("One Pointer Pokemon Searcher")

        self.initialise_vars()
        self.initialise_completer()
        self.initialise_connections()

        self.populate_pokemon_list()

    def initialise_vars(self):
        self.pokemon = {}
        self.applied_filters = []

        self.trait_sorted = False
        self.selected_trait = None

        pokemon_moves = set()
        pokemon_names = []
        pokemon_types = ["Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying",
                         "Ghost", "Grass", "Ground", "Ice", "Normal", "Psychic", "Poison", "Rock",
                         "Steel", "Water"]
        pokemon_abilities = set()

        try:
            with open(FILTERED_POKEDEX_PATH, 'r') as f:
                pokedex = json.load(f)
            with open(FILTERED_LEARNSET_PATH, 'r') as f:
                learnset_data = json.load(f)

            for pokemon, data in pokedex.items():
                num = data.get("num", -1)
                name = data.get("name", "")
                types = data.get("types", [])

                abilities = data.get("abilities", {}).items()
                base_abilities = []
                hidden_abilities = []
                for key, value in abilities:
                    if key == 'H':
                        hidden_abilities.append(value)
                    else:
                        base_abilities.append(value)

                stats = list(data.get("baseStats", {}).values())
                moves = learnset_data.get(pokemon, [])

                pokemon_obj = PokemonData(
                    name=name,
                    types=types,
                    base_abilities=base_abilities,
                    hidden_abilities=hidden_abilities,
                    stats=stats,
                    moves=moves
                )
                self.pokemon[num] = pokemon_obj

            for moves in learnset_data.values():
                pokemon_moves.update(moves)

            for pokemon, data in pokedex.items():
                name = pokemon.capitalize()
                pokemon_names.append(name)

                abilities = data.get("abilities", {}).items()
                for key, value in abilities:
                        pokemon_abilities.add(value)
            
            self.pokemon_moves = sorted(pokemon_moves)
            self.pokemon_names = sorted(pokemon_names)
            self.pokemon_types = sorted(pokemon_types)
            self.pokemon_abilities = sorted(pokemon_abilities)
                
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")

    def initialise_completer(self):
        self.completer = QCompleter(self)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.activated.connect(self.add_to_filter_list)
        self.searchBar.setCompleter(self.completer)
    
    def initialise_connections(self):
        self.clearSearchButton.clicked.connect(self.clear_search)
        self.searchBar.textChanged.connect(self.filter_pokemon)
        self.nameLabel.clicked.connect(lambda: self.sort_by_label("name"))
        self.hpLabel.clicked.connect(lambda: self.sort_by_label("hp"))
        self.atkLabel.clicked.connect(lambda: self.sort_by_label("atk"))
        self.defLabel.clicked.connect(lambda: self.sort_by_label("def"))
        self.spaLabel.clicked.connect(lambda: self.sort_by_label("spa"))
        self.spdLabel.clicked.connect(lambda: self.sort_by_label("spd"))
        self.speLabel.clicked.connect(lambda: self.sort_by_label("spe"))
        self.bstLabel.clicked.connect(lambda: self.sort_by_label("bst"))

    def populate_pokemon_list(self, order=None, reverse=False):
        self.pokemonListWidget.clear()

        def sort_key(item):
            _, pokemon = item
            if order is None: # default number order
                return 0
            elif order < 6: # one of the 6 stats
                return pokemon.stats[order]
            elif order == 6: # bst
                return sum(pokemon.stats)
            elif order == 7: # name
                return pokemon.name
            return 0

        sorted_items = sorted(self.pokemon.items(), key=sort_key, reverse=reverse if order != 7 else not reverse)
        # makes it sort from highest to lowest, apart from name, then goes alphabetical

        for pokemon_num, pokemon in sorted_items:
            custom_widget = PokemonListItem(pokemon)
            list_item = QListWidgetItem(self.pokemonListWidget)
            list_item.setSizeHint(custom_widget.sizeHint())
            self.pokemonListWidget.addItem(list_item)
            self.pokemonListWidget.setItemWidget(list_item, custom_widget)

    def clear_search(self):
        self.searchBar.clear()
        self.applied_filters = []

        for i in reversed(range(self.filterLayout.count())):
            item = self.filterLayout.itemAt(i)
            widget = item.widget()

            if widget is None:
                continue

            self.filterLayout.takeAt(i)
            widget.deleteLater()

        self.update_pokemon_list()

    def filter_pokemon(self, text):
        if len(text) < 3:
            self.completer.setModel(QStringListModel([]))
            return

        def get_filtered_list(items, label):
            return [f"{item} - {label}" for item in items]

        filter_list = []

        if self.pokemonCheckbox.isChecked():
            filter_list += get_filtered_list(self.pokemon_names, "Pokemon")

        if self.movesCheckbox.isChecked():
            filter_list += get_filtered_list(self.pokemon_moves, "Move")

        if self.typesCheckbox.isChecked():
            filter_list += get_filtered_list(self.pokemon_types, "Type")

        if self.abilitiesCheckbox.isChecked():
            filter_list += get_filtered_list(self.pokemon_abilities, "Ability")

        if not filter_list:
            filter_list = (
                get_filtered_list(self.pokemon_names, "Pokemon")
                + get_filtered_list(self.pokemon_moves, "Move")
                + get_filtered_list(self.pokemon_types, "Type")
                + get_filtered_list(self.pokemon_abilities, "Ability")
            )

        refined_list = [item for item in filter_list if text.lower() in item.lower()]

        self.completer.setModel(QStringListModel(refined_list))

    def sort_by_label(self, trait: str):
        label: ClickableLabel = getattr(self, f"{trait}Label")

        if not hasattr(self, "sorting_states"):
            self.sorting_states = {}

        current_state = self.sorting_states.get(trait, 0)

        # Show a loading dialog
        loading_dialog = QProgressDialog("Sorting Pokémon...", None, 0, 0, self)
        loading_dialog.setWindowModality(Qt.ApplicationModal)
        loading_dialog.setCancelButton(None)
        loading_dialog.setMinimumDuration(0)
        loading_dialog.setRange(0, 0)  # Indeterminate progress
        loading_dialog.show()

        # Process events to keep the UI responsive
        loop = QEventLoop()
        QTimer.singleShot(100, loop.quit)  # Allow the dialog to render
        loop.exec()

        # Perform sorting based on the current state
        if current_state == 0:
            # First click: Sort in ascending order
            label.highlight(True)
            self.sorting_states[trait] = 1
            self.sort_pokemon_list(trait, reverse=False)
        elif current_state == 1:
            # Second click: Sort in descending order
            label.highlight(True)
            self.sorting_states[trait] = 2
            self.sort_pokemon_list(trait, reverse=True)
        else:
            # Third click: Reset to default order
            label.highlight(False)
            self.sorting_states[trait] = 0
            self.populate_pokemon_list()  # Reset to the original order

        # Reset other labels' states
        for other_trait, state in self.sorting_states.items():
            if other_trait != trait and state != 0:
                other_label: ClickableLabel = getattr(self, f"{other_trait}Label")
                other_label.highlight(False)
                self.sorting_states[other_trait] = 0

        # Close the loading dialog after sorting is complete
        loading_dialog.close()

    def sort_pokemon_list(self, trait: str, reverse):
        self.pokemonListWidget.clear()
        stats = ["hp","atk","def","spa","spd","spe","bst","name"]
        self.populate_pokemon_list(stats.index(trait), reverse)

    def add_to_filter_list(self, selected_item):
        self.applied_filters.append(selected_item)

        filter_widget = QWidget(self)
        filter_layout = QHBoxLayout(filter_widget)
        filter_layout.setContentsMargins(2, 2, 2, 2)
        filter_layout.setSpacing(5)
        filter_layout.setAlignment(Qt.AlignLeft)

        filter_label = QLabel(selected_item, filter_widget)
        filter_label.setStyleSheet(
            """
            color: black;
            font-size: 10px;
            background-color: rgba(211, 211, 211, 0.8);
            border-radius: 5px;
            padding: 2px;
            """
        )
        filter_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        filter_layout.addWidget(filter_label)

        remove_label = QLabel(filter_widget)
        remove_label.setText("X")
        remove_label.setAlignment(Qt.AlignCenter)
        remove_label.setStyleSheet(
            """
            color: rgba(211, 211, 211, 0.8);
            background-color: rgba(255, 0, 0, 0.2);
            border-radius: 8px;
            font-size: 10px;
            width: 16px;
            height: 16px;
            """
        )
        remove_label.setFixedSize(16, 16)
        filter_layout.addWidget(remove_label)
        spacer_index = self.filterLayout.count() - 1
        self.filterLayout.insertWidget(spacer_index, filter_widget)

        remove_label.mousePressEvent = lambda event: self.remove_filter(filter_widget, selected_item)

        QTimer.singleShot(10, lambda: self.searchBar.setText(""))
        self.update_pokemon_list()

    def remove_filter(self, filter_widget, selected_item):
        if selected_item in self.applied_filters:
            self.applied_filters.remove(selected_item)

        self.filterLayout.removeWidget(filter_widget)
        filter_widget.deleteLater()

        self.update_pokemon_list()

    def update_pokemon_list(self):
        for i in range(self.pokemonListWidget.count()):
            list_item = self.pokemonListWidget.item(i)
            custom_widget = self.pokemonListWidget.itemWidget(list_item)

            pokemon_data = custom_widget.pokemon_data

            name = pokemon_data.name
            types = pokemon_data.types
            base_abilities = pokemon_data.base_abilities
            hidden_abilities = pokemon_data.hidden_abilities
            moves = pokemon_data.moves

            matches_filter = True
            for filter_item in self.applied_filters:
                keyword, category = filter_item.split(" - ")
                keyword = keyword.strip().lower()
                category = category.strip().lower()

                if category == "pokemon" and keyword not in name.lower():
                    matches_filter = False
                elif category == "type" and keyword not in [t.lower() for t in types]:
                    matches_filter = False
                elif category == "ability" and keyword not in [a.lower() for a in base_abilities + hidden_abilities]:
                    matches_filter = False
                elif category == "move" and keyword not in [m.lower() for m in moves]:
                    matches_filter = False

            list_item.setHidden(not matches_filter)

def handle_exception(exc_type, exc_value, exc_traceback):
    import traceback
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    print("=====================================================")
    traceback.print_exception(exc_type, exc_value, exc_traceback)
    print("=====================================================")

def main():
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon('assets/images/...'))
    #icon = QPixmap('assets/images/...')
    #resized_icon = icon.scaled(icon.size() * 0.5, Qt.KeepAspectRatio)
    #spl = QSplashScreen(resized_icon)
    #spl.show()
    #spl.activateWindow()
    window = MainWindow()
    #window.loaded.connect(lambda: spl.finish(window))
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    sys.excepthook = handle_exception
    main()