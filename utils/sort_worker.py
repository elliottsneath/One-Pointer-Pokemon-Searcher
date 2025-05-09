from PySide6.QtCore import QThread, Signal

class SortWorker(QThread):
    sorting_done = Signal(list)  # Signal to emit the sorted items

    def __init__(self, pokemon_items, trait, reverse):
        super(SortWorker, self).__init__()
        self.pokemon_items = pokemon_items
        self.trait = trait
        self.reverse = reverse

    def run(self):
        def sorting_key(item):
            _, custom_widget = item
            pokemon_data = custom_widget.pokemon_data
            if self.trait == "name":
                return pokemon_data.name.lower()
            elif self.trait == "hp":
                return pokemon_data.stats[0]
            elif self.trait == "atk":
                return pokemon_data.stats[1]
            elif self.trait == "def":
                return pokemon_data.stats[2]
            elif self.trait == "spa":
                return pokemon_data.stats[3]
            elif self.trait == "spd":
                return pokemon_data.stats[4]
            elif self.trait == "spe":
                return pokemon_data.stats[5]
            elif self.trait == "bst":
                return sum(pokemon_data.stats)
            return 0

        sorted_items = sorted(self.pokemon_items, key=sorting_key, reverse=self.reverse)
        self.sorting_done.emit(sorted_items) 