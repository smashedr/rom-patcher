# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Shane\IdeaProjects\rom-patcher-gui\gui\help.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelpDialog(object):
    def setupUi(self, HelpDialog):
        HelpDialog.setObjectName("HelpDialog")
        HelpDialog.resize(446, 325)
        HelpDialog.setMinimumSize(QtCore.QSize(446, 325))
        self.buttonBox = QtWidgets.QDialogButtonBox(HelpDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 290, 421, 21))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(HelpDialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 421, 231))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(HelpDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(HelpDialog)
        self.buttonBox.accepted.connect(HelpDialog.accept)
        self.buttonBox.rejected.connect(HelpDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HelpDialog)

    def retranslateUi(self, HelpDialog):
        _translate = QtCore.QCoreApplication.translate
        HelpDialog.setWindowTitle(_translate("HelpDialog", "Help - ROM Patcher"))
        self.label.setText(_translate("HelpDialog", "<p>This is a high level application designed to make patching ROM\'s easier. It was designed to work with SMW Central but should work with any remote or local file or archive.</p>\n"
"<ol>\n"
"    <li>\n"
"        Find a ROM Hack from SMW Central (or anywhere else):<br>\n"
"        <a href=\"https://www.smwcentral.net/?p=section&s=smwhacks\" target=\"_blank\">https://www.smwcentral.net/?p=section&s=smwhacks</a>\n"
"    </li>\n"
"    <li>\n"
"        Right click on the Download link and Copy Link Location.\n"
"    </li>\n"
"    <li>\n"
"        Paste the Download link into the first box.\n"
"    </li>\n"
"    <li>\n"
"        Locate the location to your source ROM file in the second box.\n"
"    </li>\n"
"    <li>\n"
"        Choose the output directory for the patched ROM file in the third box.\n"
"    </li>\n"
"    <li>\n"
"        Click the \"Patch ROM\" button and wait for it to finish.\n"
"    </li>\n"
"    <li>\n"
"        The finished rom will show up in the status box. You can click \"Open Directory\" to open the directory of the finished rom.\n"
"    </li>\n"
"</ol>\n"
"<p>\n"
"    For additional Help see the README.md on GitHub:\n"
"</p>\n"
"<ul>\n"
"    <li>\n"
"        GitHub: <a href=\"https://github.com/smashedr/rom-patcher\" target=\"_blank\">https://github.com/smashedr/rom-patcher</a>\n"
"    </li>\n"
"</ul>"))
        self.label_2.setText(_translate("HelpDialog", "ROM Patcher Help"))

