# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_board(object):
    def setupUi(self, board):
        board.setObjectName("board")
        board.resize(700, 863)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(board.sizePolicy().hasHeightForWidth())
        board.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/emoji_x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        board.setWindowIcon(icon)
        self.boardWidget = QtWidgets.QTableWidget(board)
        self.boardWidget.setGeometry(QtCore.QRect(50, 200, 601, 601))
        self.boardWidget.setStyleSheet("\n"
                                       "                    QPushButton#boardButtonTop\n"
                                       "                    {\n"
                                       "                    border-bottom:3px solid black;\n"
                                       "                    }\n"
                                       "                    QTableWidget::item#7\n"
                                       "                    {\n"
                                       "                    border:3px solid black;\n"
                                       "                    }\n"
                                       "                    QTableWidget {\n"
                                       "                    border: 0px solid black;\n"
                                       "                    }\n"
                                       "                ")
        self.boardWidget.setObjectName("boardWidget")
        self.boardWidget.setColumnCount(3)
        self.boardWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.boardWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardWidget.setHorizontalHeaderItem(2, item)
        self.statusLabel = QtWidgets.QLabel(board)
        self.statusLabel.setGeometry(QtCore.QRect(50, 140, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.statusLabel.setFont(font)
        self.statusLabel.setAcceptDrops(True)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.playerLabelX = QtWidgets.QLabel(board)
        self.playerLabelX.setGeometry(QtCore.QRect(50, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.playerLabelX.setFont(font)
        self.playerLabelX.setAcceptDrops(True)
        self.playerLabelX.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabelX.setObjectName("playerLabelX")
        self.playerLabelO = QtWidgets.QLabel(board)
        self.playerLabelO.setGeometry(QtCore.QRect(250, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.playerLabelO.setFont(font)
        self.playerLabelO.setAcceptDrops(True)
        self.playerLabelO.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabelO.setObjectName("playerLabelO")
        self.playerLabelD = QtWidgets.QLabel(board)
        self.playerLabelD.setGeometry(QtCore.QRect(450, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.playerLabelD.setFont(font)
        self.playerLabelD.setAcceptDrops(True)
        self.playerLabelD.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabelD.setObjectName("playerLabelD")
        self.scoreO = QtWidgets.QLabel(board)
        self.scoreO.setGeometry(QtCore.QRect(250, 90, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.scoreO.setFont(font)
        self.scoreO.setAcceptDrops(True)
        self.scoreO.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreO.setObjectName("scoreO")
        self.scoreX = QtWidgets.QLabel(board)
        self.scoreX.setGeometry(QtCore.QRect(50, 90, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.scoreX.setFont(font)
        self.scoreX.setAcceptDrops(True)
        self.scoreX.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreX.setObjectName("scoreX")
        self.scoreD = QtWidgets.QLabel(board)
        self.scoreD.setGeometry(QtCore.QRect(450, 90, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.scoreD.setFont(font)
        self.scoreD.setAcceptDrops(True)
        self.scoreD.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreD.setObjectName("scoreD")
        self.resetButton = QtWidgets.QPushButton(board)
        self.resetButton.setGeometry(QtCore.QRect(40, 820, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.returnToMenu = QtWidgets.QPushButton(board)
        self.returnToMenu.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.returnToMenu.setFont(font)
        self.returnToMenu.setObjectName("returnToMenu")
        self.loadingMessage = QtWidgets.QLabel(board)
        self.loadingMessage.setGeometry(QtCore.QRect(0, 0, 701, 861))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loadingMessage.setFont(font)
        self.loadingMessage.setAcceptDrops(True)
        self.loadingMessage.setAutoFillBackground(True)
        self.loadingMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingMessage.setObjectName("loadingMessage")

        self.retranslateUi(board)
        QtCore.QMetaObject.connectSlotsByName(board)

    def retranslateUi(self, board):
        _translate = QtCore.QCoreApplication.translate
        board.setWindowTitle(_translate("board", "Noughts and Crosses"))
        item = self.boardWidget.verticalHeaderItem(0)
        item.setText(_translate("board", "New Row"))
        item = self.boardWidget.verticalHeaderItem(1)
        item.setText(_translate("board", "New Row"))
        item = self.boardWidget.verticalHeaderItem(2)
        item.setText(_translate("board", "New Row"))
        item = self.boardWidget.horizontalHeaderItem(0)
        item.setText(_translate("board", "New Column"))
        item = self.boardWidget.horizontalHeaderItem(1)
        item.setText(_translate("board", "New Column"))
        item = self.boardWidget.horizontalHeaderItem(2)
        item.setText(_translate("board", "New Column"))
        self.statusLabel.setText(_translate("board", "Thinking..."))
        self.playerLabelX.setText(_translate("board", "Cross"))
        self.playerLabelO.setText(_translate("board", "Nought"))
        self.playerLabelD.setText(_translate("board", "Draw"))
        self.scoreO.setText(_translate("board", "Nought"))
        self.scoreX.setText(_translate("board", "Cross"))
        self.scoreD.setText(_translate("board", "Draw"))
        self.resetButton.setText(_translate("board", "Play Again"))
        self.returnToMenu.setText(_translate("board", "Return to Menu"))
        self.loadingMessage.setText(_translate("board", "Loading game..."))
