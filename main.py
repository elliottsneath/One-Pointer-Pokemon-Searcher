import sys
import json
import os
from assets.ui.pokemon_list_item import PokemonListItem
from data.pokemon_obj import PokemonData
from assets.ui.main_ui import Ui_PokemonSearcher
from assets.ui.pokemon_popup_ui import Ui_PokemonPopup
from assets.ui.clickable_label import ClickableLabel
from PySide6.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QCompleter, QWidget, \
                              QHBoxLayout, QDialog, QLabel, QSizePolicy, QSplashScreen
from PySide6.QtGui import Qt, QPixmap, QColor, QIcon
from PySide6.QtCore import QStringListModel, QTimer, Signal

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILTERED_POKEDEX_PATH = os.path.join(BASE_DIR, "data/filtered_pokedex.json")
FILTERED_LEARNSET_PATH = os.path.join(BASE_DIR, "data/filtered_learnset.json")
CONFIG_FILE_PATH = os.path.join(BASE_DIR, "data/config.json")

"""
TODO:
    Add favourites with config file
"""

class MainWindow(QMainWindow, Ui_PokemonSearcher):
    loaded = Signal()
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("One Pointer Pokemon Searcher")

        self.initialise_vars()
        self.initialise_completer()
        self.initialise_connections()

        self.update_filtered_pokemon()

        self.loaded.emit()

    def initialise_vars(self):
        self.master_list = []
        self.filtered_sorted_list = []
        self.applied_filters = []
        self.selected_trait = None
        self.trait_reverse = True

        self.all_names = []
        self.all_moves = set()
        self.all_types = ["Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying",
                         "Ghost", "Grass", "Ground", "Ice", "Normal", "Psychic", "Poison", "Rock",
                         "Steel", "Water"]
        self.all_abilities = set()

        self.load_pokemon_data()

    def load_pokemon_data(self):
        try:
            with open(FILTERED_POKEDEX_PATH, 'r') as f:
                pokedex = json.load(f)
            with open(FILTERED_LEARNSET_PATH, 'r') as f:
                learnset_data = json.load(f)
            with open(CONFIG_FILE_PATH, 'r') as f:
                favourites = json.load(f)

            self.highest_stats = [-float('inf')] * 6
            self.lowest_stats = [float('inf')] * 6

            for pokemon, data in pokedex.items():
                #get data from each mon in json
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

                favourite = True if name in favourites.get("favourites") else False

                # update highest and lowest stats
                for i, stat in enumerate(stats):
                    if stat > self.highest_stats[i]:
                        self.highest_stats[i] = stat
                    if stat < self.lowest_stats[i]:
                        self.lowest_stats[i] = stat

                # create pokemon object
                pokemon_obj = PokemonData(
                    num=num,
                    name=name,
                    types=types,
                    base_abilities=base_abilities,
                    hidden_abilities=hidden_abilities,
                    stats=stats,
                    moves=moves,
                    favourite=favourite
                )

                # populate lists of pokemon
                self.master_list.append(pokemon_obj)
                self.filtered_sorted_list.append(pokemon_obj)

                # get lists of all possible moves, names, abilities
                self.all_names.append(name)
                abilities = data.get("abilities", {}).items()
                for _, value in abilities:
                    self.all_abilities.add(value)

            for moves in learnset_data.values():
                self.all_moves.update(moves)

        except FileNotFoundError as e:
            print(f"Error: {e}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")

    def initialise_completer(self):
        self.completer = QCompleter(self)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchContains)
        #self.completer.activated.connect(self.add_to_applied_filters)
        self.completer.highlighted.connect(self.add_to_applied_filters)
        self.searchBar.setCompleter(self.completer)

    def initialise_connections(self):
        self.pokemonListWidget.itemClicked.connect(self.open_pokemon_popup)
        self.clearFiltersButton.clicked.connect(self.clear_filters)
        self.searchBar.textChanged.connect(self.filter_completer)
        self.nameLabel.clicked.connect(lambda: self.sort_by_trait("name"))
        self.hpLabel.clicked.connect(lambda: self.sort_by_trait("hp"))
        self.atkLabel.clicked.connect(lambda: self.sort_by_trait("atk"))
        self.defLabel.clicked.connect(lambda: self.sort_by_trait("def"))
        self.spaLabel.clicked.connect(lambda: self.sort_by_trait("spa"))
        self.spdLabel.clicked.connect(lambda: self.sort_by_trait("spd"))
        self.speLabel.clicked.connect(lambda: self.sort_by_trait("spe"))
        self.bstLabel.clicked.connect(lambda: self.sort_by_trait("bst"))

    def add_to_applied_filters(self, selected_item):
        keyword, category = selected_item.split(" - ")
        keyword = keyword.strip().lower()
        category = category.strip().lower()
        self.applied_filters.append((keyword, category))

        self.add_filter_to_ui(selected_item)
        self.update_filtered_pokemon()

    def add_filter_to_ui(self, selected_item):
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

    def remove_filter(self, filter_widget, selected_item):
        keyword, category = selected_item.split(" - ")
        keyword = keyword.strip().lower()
        category = category.strip().lower()
        if (keyword, category) in self.applied_filters:
            self.applied_filters.remove((keyword, category))

        self.filterLayout.removeWidget(filter_widget)
        filter_widget.deleteLater()

        self.update_filtered_pokemon()

    def clear_filters(self):
        self.applied_filters = []
        self.update_filtered_pokemon()

    def sort_by_trait(self, trait):
        label: ClickableLabel = getattr(self, f"{trait}Label")

        if self.selected_trait == None:
            label.highlight(True)
            self.selected_trait = trait
            self.trait_reverse = True

        elif self.selected_trait == trait:
            if self.trait_reverse == False:
                label.highlight(False)
                self.selected_trait = None
                self.trait_reverse = True
            else:
                self.trait_reverse = False
        
        else:
            label.highlight(True)
            prev_label: ClickableLabel = getattr(self, f"{self.selected_trait}Label")
            prev_label.highlight(False)
            self.selected_trait = trait
            self.trait_reverse = True

        self.update_filtered_pokemon()

    def update_filtered_pokemon(self):
        self.filtered_sorted_list = []
        # filter first then sort, so we are sorting with less
        for pokemon in self.master_list:
            if self.applied_filters == []:
                self.filtered_sorted_list = self.master_list
                break

            pokemon: PokemonData
            matches_filter = True
            for keyword, category in self.applied_filters:
                if category == "pokemon" and keyword not in pokemon.name.lower():
                    matches_filter = False
                elif category == "type" and keyword not in [t.lower() for t in pokemon.types]:
                    matches_filter = False
                elif category == "ability" and keyword not in [a.lower() for a in pokemon.base_abilities + pokemon.hidden_abilities]:
                    matches_filter = False
                elif category == "move" and keyword not in [m.lower() for m in pokemon.moves]:
                    matches_filter = False

            if matches_filter:
                self.filtered_sorted_list.append(pokemon)

        # now we have all filtered pokemon in self.filtered_sorted_list
        if self.selected_trait == None or self.selected_trait == "num":
            sort_key = lambda pokemon: pokemon.num
            reverse = not self.trait_reverse
        elif self.selected_trait == "name":
            sort_key = lambda pokemon: pokemon.name
            reverse = not self.trait_reverse
        elif self.selected_trait == "bst":
            sort_key = lambda pokemon: sum(pokemon.stats)
            reverse = self.trait_reverse 
        else:
            stats = ["hp","atk","def","spa","spd","spe"]
            sort_key = lambda pokemon: pokemon.stats[stats.index(self.selected_trait)]
            reverse = self.trait_reverse        

        self.filtered_sorted_list = sorted(self.filtered_sorted_list, key=sort_key, reverse=reverse)
        self.filtered_sorted_list = [p for p in self.filtered_sorted_list if p.favourite] + [p for p in self.filtered_sorted_list if not p.favourite]
        
        self.update_pokemon_list_ui()

    def update_pokemon_list_ui(self):
        self.pokemonListWidget.clear()

        for pokemon in self.filtered_sorted_list:
            custom_widget = PokemonListItem(pokemon)
            list_item = QListWidgetItem(self.pokemonListWidget)
            list_item.setSizeHint(custom_widget.sizeHint())
            self.pokemonListWidget.addItem(list_item)
            self.pokemonListWidget.setItemWidget(list_item, custom_widget)

    def filter_completer(self, text: str):
        def get_filtered_list(items, label):
            return [f"{item} - {label}" for item in items]

        filter_list = []

        if self.pokemonCheckbox.isChecked():
            filter_list += get_filtered_list(self.all_names, "Pokemon")

        if self.movesCheckbox.isChecked():
            filter_list += get_filtered_list(self.all_moves, "Move")

        if self.typesCheckbox.isChecked():
            filter_list += get_filtered_list(self.all_types, "Type")

        if self.abilitiesCheckbox.isChecked():
            filter_list += get_filtered_list(self.all_abilities, "Ability")

        if not filter_list:
            filter_list = (
                get_filtered_list(self.all_names, "Pokemon")
                + get_filtered_list(self.all_moves, "Move")
                + get_filtered_list(self.all_types, "Type")
                + get_filtered_list(self.all_abilities, "Ability")
            )

        refined_list = [item for item in filter_list if text.lower() in item.lower()]

        self.completer.setModel(QStringListModel(refined_list))

    def open_pokemon_popup(self, item):
        index = self.pokemonListWidget.row(item)
        selected_pokemon = self.filtered_sorted_list[index]

        self.popup = QDialog(self)
        self.ui = Ui_PokemonPopup()
        self.ui.setupUi(self.popup)

        self.ui.lineEdit.textChanged.connect(lambda text: self.update_moves_in_popup(text, selected_pokemon))
        self.ui.starLabel.clicked.connect(lambda: self.update_favourites(selected_pokemon))

        self.ui.nameLabel.setText(selected_pokemon.name)
        
        star_png = "star_filled.png" if selected_pokemon.favourite else "star.png"
        png_path = os.path.join("assets", "icons", star_png)
        self.ui.starLabel.setPixmap(QPixmap(png_path).scaled(36, 36))
        
        if len(selected_pokemon.types) < 2:
            type = selected_pokemon.types[0]
            svg_path = os.path.join("assets", "icons", f"{type.lower()}.svg")
            pixmap = QPixmap(svg_path)
            if not pixmap.isNull():
                self.ui.type1Label.setPixmap(pixmap.scaled(36, 36))
                self.ui.type2Label.setText("")
            else:
                self.ui.type1Label.setText(type)
                self.ui.type2Label.setText("")
        else:
            type1 = selected_pokemon.types[0]
            type2 = selected_pokemon.types[1]
            svg_path1 = os.path.join("assets", "icons", f"{type1.lower()}.svg")
            svg_path2 = os.path.join("assets", "icons", f"{type2.lower()}.svg")
            pixmap1 = QPixmap(svg_path1)
            pixmap2 = QPixmap(svg_path2)
            if not pixmap1.isNull() and not pixmap2.isNull():
                self.ui.type1Label.setPixmap(pixmap1.scaled(36, 36))
                self.ui.type2Label.setPixmap(pixmap2.scaled(36, 36))
            else:
                self.ui.type1Label.setText(type1)
                self.ui.type2Label.setText(type2)

        stats = selected_pokemon.stats

        self.ui.hpNumLabel.setText(str(stats[0]))
        self.ui.atkNumLabel.setText(str(stats[1]))
        self.ui.defNumLabel.setText(str(stats[2]))
        self.ui.spaNumLabel.setText(str(stats[3]))
        self.ui.spdNumLabel.setText(str(stats[4]))
        self.ui.speNumLabel.setText(str(stats[5]))

        stat_bars = [
            self.ui.hpStatBar,
            self.ui.atkStatBar,
            self.ui.defStatBar,
            self.ui.spaStatBar,
            self.ui.spdStatBar,
            self.ui.speStatBar,
        ]

        for i, stat in enumerate(stats):
            lowest = self.lowest_stats[i]
            highest = self.highest_stats[i]

            normalized_value = (stat - lowest) / (highest - lowest) if highest > lowest else 0

            red = int(255 * (1 - normalized_value))
            green = int(255 * normalized_value)
            color = QColor(red, green, 0)

            stat_bars[i].set_value(stat, max_stat=highest)
            stat_bars[i].color = color
            stat_bars[i].update()

        self.ui.moveListWidget.clear()
        for move in selected_pokemon.moves:
            self.ui.moveListWidget.addItem(move)

        self.popup.exec()
        self.update_filtered_pokemon()

    def update_favourites(self, pokemon):
        pokemon.favourite = not pokemon.favourite
        self.ui.starLabel.change_star(pokemon.favourite)

    def update_moves_in_popup(self, text: str, selected_pokemon):
        self.ui.moveListWidget.clear()
        for move in selected_pokemon.moves:
            if text in move:
                self.ui.moveListWidget.addItem(move)

    def closeEvent(self, event):
        try:
            favourite_names = [pokemon.name for pokemon in self.master_list if pokemon.favourite]

            with open(CONFIG_FILE_PATH, 'w') as f:
                json.dump({"favourites": favourite_names}, f, indent=4)

            print("Favourites saved successfully.")
        except Exception as e:
            print(f"Error saving favourites: {e}")

        event.accept()
        

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
    app.setWindowIcon(QIcon('assets/icons/JCB_Logo'))

    icon = QPixmap('assets/icons/JCB_Logo')
    resized_icon = icon.scaled(icon.size() * 0.5, Qt.KeepAspectRatio)

    spl = QSplashScreen(resized_icon)
    spl.show()
    spl.activateWindow()

    window = MainWindow()
    window.loaded.connect(lambda: spl.finish(window))
    window.show()
    spl.finish(window)

    sys.exit(app.exec())

if __name__ == '__main__':
    sys.excepthook = handle_exception
    main()