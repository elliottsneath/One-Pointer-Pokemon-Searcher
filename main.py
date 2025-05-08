import sys
import json
import os
from utils.pokemon_list_item import PokemonListItem
from assets.ui.main_ui import Ui_PokemonSearcher
from PySide6.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QCompleter, QWidget, \
                              QHBoxLayout, QPushButton, QLabel
from PySide6.QtGui import Qt
from PySide6.QtCore import QStringListModel, QTimer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILTERED_POKEDEX_PATH = os.path.join(BASE_DIR, "filtered_pokedex.json")
FILTERED_LEARNSET_PATH = os.path.join(BASE_DIR, "filtered_learnset.json")

class MainWindow(QMainWindow, Ui_PokemonSearcher):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("One Pointer Pokemon Searcher")

        self.initialise_assets()
        self.initialise_completer()
        self.initialise_connections()

        self.populate_pokemon_list()

    def initialise_assets(self):
        self.applied_filters = []

        pokemon_moves = set()
        pokemon_names = []
        pokemon_types = ["Normal", "Fire", "Water", "Grass", "Flying", "Fighting", "Poison", "Electric", "Ground",
                         "Rock", "Psychic", "Ice", "Bug", "Ghost", "Steel", "Dragon", "Dark", "Fairy"]
        pokemon_abilities = set()

        try:
            with open(FILTERED_LEARNSET_PATH, 'r') as f:
                learnset_data = json.load(f)

            for _, data in learnset_data.items():
                moves = data.get("learnset", {})
                for move in moves.keys():
                    pokemon_moves.add(move)
            
            self.pokemon_moves = sorted(pokemon_moves)

        except FileNotFoundError:
            print(f"Error: {FILTERED_LEARNSET_PATH} not found.")
        except json.JSONDecodeError:
            print(f"Error parsing JSON in {FILTERED_LEARNSET_PATH}.")


        try:
            with open(FILTERED_POKEDEX_PATH, 'r') as f:
                pokedex = json.load(f)

            for pokemon, data in pokedex.items():
                name = pokemon.capitalize()
                pokemon_names.append(name)

                abilities = data.get("abilities", {}).items()
                for key, value in abilities:
                        pokemon_abilities.add(value)
            
            self.pokemon_names = sorted(pokemon_names)
            self.pokemon_types = sorted(pokemon_types)
            self.pokemon_abilities = sorted(pokemon_abilities)

        except FileNotFoundError:
            print(f"Error: {FILTERED_LEARNSET_PATH} not found.")
        except json.JSONDecodeError:
            print(f"Error parsing JSON in {FILTERED_LEARNSET_PATH}.")

    def initialise_completer(self):
        self.completer = QCompleter(self)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.activated.connect(self.add_to_filter_list)
        self.searchBar.setCompleter(self.completer)
    
    def initialise_connections(self):
        self.clearSearchButton.clicked.connect(self.clear_search)
        self.searchBar.textChanged.connect(self.filter_pokemon)

    def populate_pokemon_list(self):
        try:
            with open(FILTERED_POKEDEX_PATH, 'r') as f:
                pokedex = json.load(f)

            for pokemon, data in pokedex.items():
                name = pokemon.capitalize()

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

                custom_widget = PokemonListItem(name, types, base_abilities, hidden_abilities, stats)

                list_item = QListWidgetItem(self.pokemonListWidget)
                list_item.setSizeHint(custom_widget.sizeHint())

                self.pokemonListWidget.addItem(list_item)
                self.pokemonListWidget.setItemWidget(list_item, custom_widget)

        except FileNotFoundError as e:
            print(f"Error: {e}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")


    def clear_search(self):
        self.searchBar.clear()

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


    def add_to_filter_list(self, selected_item):
        self.applied_filters.append(selected_item)
        print(f"Added to filter list: {selected_item}")

        filter_widget = QWidget(self)
        filter_widget.setStyleSheet("background-color: lightgrey; border-radius: 5px; padding: 5px;")
        filter_layout = QHBoxLayout(filter_widget)
        filter_layout.setContentsMargins(5, 5, 5, 5)
        filter_layout.setSpacing(5)

        filter_label = QLabel(selected_item, filter_widget)
        filter_label.setStyleSheet("color: black;")
        filter_layout.addWidget(filter_label)

        remove_button = QPushButton("X", filter_widget)
        remove_button.setStyleSheet(
            "background-color: red; color: white; border: none; border-radius: 3px; padding: 2px 5px;"
        )
        remove_button.setFixedSize(20, 20)
        filter_layout.addWidget(remove_button)

        self.filterLayout.addWidget(filter_widget)

        remove_button.clicked.connect(lambda: self.remove_filter(filter_widget, selected_item))

        QTimer.singleShot(10, lambda: self.searchBar.setText(""))

    def remove_filter(self, filter_widget, selected_item):
        if selected_item in self.applied_filters:
            self.applied_filters.remove(selected_item)
            print(f"Removed from filter list: {selected_item}")

        self.filterLayout.removeWidget(filter_widget)
        filter_widget.deleteLater()


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
    #app.setWindowIcon(QIcon('assets/images/potato_can.png'))
    #icon = QPixmap('assets/images/potato_can.png')
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