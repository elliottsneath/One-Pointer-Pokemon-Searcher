from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout
from PySide6.QtGui import QFont, QPixmap, Qt
import os

class PokemonListItem(QWidget):
    def __init__(self, name, types, base_abilities, hidden_abilities, stats, parent=None):
        super(PokemonListItem, self).__init__(parent)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 10, 0)
        layout.setSpacing(6)

        name_label = QLabel(name)
        name_label.setFont(QFont("Arial", 12, QFont.Bold))
        name_label.setFixedWidth(120)
        name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(name_label)


        types_layout = QHBoxLayout()
        for pokemon_type in types:
            type_icon = QLabel()
            svg_path = os.path.join("assets", "icons", f"{pokemon_type.lower()}.svg")
            pixmap = QPixmap(svg_path)
            if not pixmap.isNull():
                type_icon.setPixmap(pixmap.scaled(36, 36))
            else:
                type_icon.setText(pokemon_type)
            types_layout.addWidget(type_icon)

        types_layout.setAlignment(Qt.AlignCenter)
        types_widget = QWidget()
        types_widget.setLayout(types_layout)
        types_widget.setFixedWidth(100) 
        layout.addWidget(types_widget)


        abilities_layout = QHBoxLayout()

        base_abilities_layout = QVBoxLayout()
        for ability in base_abilities:
            ability_label = QLabel(ability)
            ability_label.setFixedWidth(100)
            base_abilities_layout.addWidget(ability_label)
        abilities_layout.addLayout(base_abilities_layout)

        hidden_abilities_layout = QVBoxLayout()
        for ability in hidden_abilities:
            ability_label = QLabel(ability)
            ability_label.setFixedWidth(100)
            hidden_abilities_layout.addWidget(ability_label)
        abilities_layout.addLayout(hidden_abilities_layout)

        abilities_layout.setAlignment(Qt.AlignCenter)
        abilities_widget = QWidget()
        abilities_widget.setLayout(abilities_layout)
        abilities_widget.setFixedWidth(200) 
        layout.addWidget(abilities_widget)


        hp_label = QLabel(str(stats[0]))
        hp_label.setFixedWidth(30)
        layout.addWidget(hp_label)

        atk_label = QLabel(str(stats[1]))
        atk_label.setFixedWidth(30)
        layout.addWidget(atk_label)

        def_label = QLabel(str(stats[2]))
        def_label.setFixedWidth(30)
        layout.addWidget(def_label)

        spa_label = QLabel(str(stats[3]))
        spa_label.setFixedWidth(30)
        layout.addWidget(spa_label)

        spd_label = QLabel(str(stats[4]))
        spd_label.setFixedWidth(30)
        layout.addWidget(spd_label)

        spe_label = QLabel(str(stats[5]))
        spe_label.setFixedWidth(30)
        layout.addWidget(spe_label)

        bst_label = QLabel(str(sum(stats)))
        bst_label.setFixedWidth(30)
        layout.addWidget(bst_label)

        self.setLayout(layout)