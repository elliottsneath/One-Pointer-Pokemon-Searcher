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
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.filterLayout.addItem(self.horizontalSpacer_2)


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
        self.horizontalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMinimumSize(QSize(120, 0))
        self.label_2.setBaseSize(QSize(0, 0))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(200, 0))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMinimumSize(QSize(30, 0))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMinimumSize(QSize(30, 0))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMinimumSize(QSize(30, 0))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setMinimumSize(QSize(30, 0))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMinimumSize(QSize(30, 0))
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setMinimumSize(QSize(30, 0))
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_10)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setMinimumSize(QSize(30, 0))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_11)


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
        self.label_2.setText(QCoreApplication.translate("PokemonSearcher", u"Name", None))
        self.label.setText(QCoreApplication.translate("PokemonSearcher", u"Types", None))
        self.label_3.setText(QCoreApplication.translate("PokemonSearcher", u"Abilities", None))
        self.label_6.setText(QCoreApplication.translate("PokemonSearcher", u"HP", None))
        self.label_4.setText(QCoreApplication.translate("PokemonSearcher", u"Atk", None))
        self.label_7.setText(QCoreApplication.translate("PokemonSearcher", u"Def", None))
        self.label_8.setText(QCoreApplication.translate("PokemonSearcher", u"SpA", None))
        self.label_9.setText(QCoreApplication.translate("PokemonSearcher", u"SpD", None))
        self.label_10.setText(QCoreApplication.translate("PokemonSearcher", u"Spe", None))
        self.label_11.setText(QCoreApplication.translate("PokemonSearcher", u"BST", None))
    # retranslateUi

