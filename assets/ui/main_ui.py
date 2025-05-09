# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from assets.ui.animated_button import AnimatedHoverButton
from assets.ui.clickable_label import ClickableLabel

class Ui_PokemonSearcher(object):
    def setupUi(self, PokemonSearcher):
        if not PokemonSearcher.objectName():
            PokemonSearcher.setObjectName(u"PokemonSearcher")
        PokemonSearcher.resize(731, 600)
        self.centralwidget = QWidget(PokemonSearcher)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchBar = QLineEdit(self.centralwidget)
        self.searchBar.setObjectName(u"searchBar")

        self.horizontalLayout.addWidget(self.searchBar)

        self.clearSearchButton = AnimatedHoverButton(self.centralwidget)
        self.clearSearchButton.setObjectName(u"clearSearchButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearSearchButton.sizePolicy().hasHeightForWidth())
        self.clearSearchButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.clearSearchButton)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.filterLayout = QHBoxLayout()
        self.filterLayout.setObjectName(u"filterLayout")

        self.verticalLayout.addLayout(self.filterLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.pokemonCheckbox = QCheckBox(self.centralwidget)
        self.pokemonCheckbox.setObjectName(u"pokemonCheckbox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pokemonCheckbox.sizePolicy().hasHeightForWidth())
        self.pokemonCheckbox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.pokemonCheckbox)

        self.typesCheckbox = QCheckBox(self.centralwidget)
        self.typesCheckbox.setObjectName(u"typesCheckbox")
        sizePolicy2.setHeightForWidth(self.typesCheckbox.sizePolicy().hasHeightForWidth())
        self.typesCheckbox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.typesCheckbox)

        self.abilitiesCheckbox = QCheckBox(self.centralwidget)
        self.abilitiesCheckbox.setObjectName(u"abilitiesCheckbox")
        sizePolicy2.setHeightForWidth(self.abilitiesCheckbox.sizePolicy().hasHeightForWidth())
        self.abilitiesCheckbox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.abilitiesCheckbox)

        self.movesCheckbox = QCheckBox(self.centralwidget)
        self.movesCheckbox.setObjectName(u"movesCheckbox")
        sizePolicy2.setHeightForWidth(self.movesCheckbox.sizePolicy().hasHeightForWidth())
        self.movesCheckbox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.movesCheckbox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 10, -1)
        self.nameLabel = ClickableLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy3)
        self.nameLabel.setMinimumSize(QSize(120, 0))
        self.nameLabel.setBaseSize(QSize(0, 0))
        self.nameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.nameLabel)

        self.typeLabel = QLabel(self.centralwidget)
        self.typeLabel.setObjectName(u"typeLabel")
        sizePolicy3.setHeightForWidth(self.typeLabel.sizePolicy().hasHeightForWidth())
        self.typeLabel.setSizePolicy(sizePolicy3)
        self.typeLabel.setMinimumSize(QSize(100, 0))
        self.typeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.typeLabel)

        self.ablilityLabel = QLabel(self.centralwidget)
        self.ablilityLabel.setObjectName(u"ablilityLabel")
        sizePolicy3.setHeightForWidth(self.ablilityLabel.sizePolicy().hasHeightForWidth())
        self.ablilityLabel.setSizePolicy(sizePolicy3)
        self.ablilityLabel.setMinimumSize(QSize(200, 0))
        self.ablilityLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.ablilityLabel)

        self.hpLabel = ClickableLabel(self.centralwidget)
        self.hpLabel.setObjectName(u"hpLabel")
        sizePolicy3.setHeightForWidth(self.hpLabel.sizePolicy().hasHeightForWidth())
        self.hpLabel.setSizePolicy(sizePolicy3)
        self.hpLabel.setMinimumSize(QSize(30, 0))
        self.hpLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.hpLabel)

        self.atkLabel = ClickableLabel(self.centralwidget)
        self.atkLabel.setObjectName(u"atkLabel")
        sizePolicy3.setHeightForWidth(self.atkLabel.sizePolicy().hasHeightForWidth())
        self.atkLabel.setSizePolicy(sizePolicy3)
        self.atkLabel.setMinimumSize(QSize(30, 0))
        self.atkLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.atkLabel)

        self.defLabel = ClickableLabel(self.centralwidget)
        self.defLabel.setObjectName(u"defLabel")
        sizePolicy3.setHeightForWidth(self.defLabel.sizePolicy().hasHeightForWidth())
        self.defLabel.setSizePolicy(sizePolicy3)
        self.defLabel.setMinimumSize(QSize(30, 0))
        self.defLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.defLabel)

        self.spaLabel = ClickableLabel(self.centralwidget)
        self.spaLabel.setObjectName(u"spaLabel")
        sizePolicy3.setHeightForWidth(self.spaLabel.sizePolicy().hasHeightForWidth())
        self.spaLabel.setSizePolicy(sizePolicy3)
        self.spaLabel.setMinimumSize(QSize(30, 0))
        self.spaLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.spaLabel)

        self.spdLabel = ClickableLabel(self.centralwidget)
        self.spdLabel.setObjectName(u"spdLabel")
        sizePolicy3.setHeightForWidth(self.spdLabel.sizePolicy().hasHeightForWidth())
        self.spdLabel.setSizePolicy(sizePolicy3)
        self.spdLabel.setMinimumSize(QSize(30, 0))
        self.spdLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.spdLabel)

        self.speLabel = ClickableLabel(self.centralwidget)
        self.speLabel.setObjectName(u"speLabel")
        sizePolicy3.setHeightForWidth(self.speLabel.sizePolicy().hasHeightForWidth())
        self.speLabel.setSizePolicy(sizePolicy3)
        self.speLabel.setMinimumSize(QSize(30, 0))
        self.speLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.speLabel)

        self.bstLabel = ClickableLabel(self.centralwidget)
        self.bstLabel.setObjectName(u"bstLabel")
        sizePolicy3.setHeightForWidth(self.bstLabel.sizePolicy().hasHeightForWidth())
        self.bstLabel.setSizePolicy(sizePolicy3)
        self.bstLabel.setMinimumSize(QSize(30, 0))
        self.bstLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.bstLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pokemonListWidget = QListWidget(self.centralwidget)
        self.pokemonListWidget.setObjectName(u"pokemonListWidget")

        self.verticalLayout.addWidget(self.pokemonListWidget)

        PokemonSearcher.setCentralWidget(self.centralwidget)

        self.retranslateUi(PokemonSearcher)

        QMetaObject.connectSlotsByName(PokemonSearcher)
    # setupUi

    def retranslateUi(self, PokemonSearcher):
        PokemonSearcher.setWindowTitle(QCoreApplication.translate("PokemonSearcher", u"MainWindow", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("PokemonSearcher", u"Search Pokemon, Move, Type, Ability, etc...", None))
        self.clearSearchButton.setText(QCoreApplication.translate("PokemonSearcher", u"Clear Filters", None))
        self.label_5.setText(QCoreApplication.translate("PokemonSearcher", u"Leave all blank to search for all:", None))
        self.pokemonCheckbox.setText(QCoreApplication.translate("PokemonSearcher", u"Pokemon", None))
        self.typesCheckbox.setText(QCoreApplication.translate("PokemonSearcher", u"Types", None))
        self.abilitiesCheckbox.setText(QCoreApplication.translate("PokemonSearcher", u"Abilities", None))
        self.movesCheckbox.setText(QCoreApplication.translate("PokemonSearcher", u"Moves", None))
        self.nameLabel.setText(QCoreApplication.translate("PokemonSearcher", u"Name", None))
        self.typeLabel.setText(QCoreApplication.translate("PokemonSearcher", u"Types", None))
        self.ablilityLabel.setText(QCoreApplication.translate("PokemonSearcher", u"Abilities", None))
        self.hpLabel.setText(QCoreApplication.translate("PokemonSearcher", u"HP", None))
        self.atkLabel.setText(QCoreApplication.translate("PokemonSearcher", u"Atk", None))
        self.defLabel.setText(QCoreApplication.translate("PokemonSearcher", u"Def", None))
        self.spaLabel.setText(QCoreApplication.translate("PokemonSearcher", u"SpA", None))
        self.spdLabel.setText(QCoreApplication.translate("PokemonSearcher", u"SpD", None))
        self.speLabel.setText(QCoreApplication.translate("PokemonSearcher", u"Spe", None))
        self.bstLabel.setText(QCoreApplication.translate("PokemonSearcher", u"BST", None))
    # retranslateUi

