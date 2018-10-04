# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\raluaces\rom-patcher\gui\about.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(510, 320)
        AboutDialog.setMinimumSize(QtCore.QSize(510, 320))
        AboutDialog.setMaximumSize(QtCore.QSize(510, 320))
        self.buttonBox = QtWidgets.QDialogButtonBox(AboutDialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 290, 421, 21))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.label_2 = QtWidgets.QLabel(AboutDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(AboutDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 421, 16))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AboutDialog)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 751, 61))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(AboutDialog)
        self.label_6.setGeometry(QtCore.QRect(10, 180, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(AboutDialog)
        self.label_8.setGeometry(QtCore.QRect(20, 120, 421, 61))
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(AboutDialog)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 721, 61))
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(AboutDialog)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(AboutDialog)
        self.buttonBox.accepted.connect(AboutDialog.accept)
        self.buttonBox.rejected.connect(AboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About - ROM Patcher"))
        self.label_2.setText(_translate("AboutDialog", "About ROM Patcher"))
        self.label_4.setText(_translate("AboutDialog", "The following software was used in the creation of this tool:"))
        self.label_5.setText(_translate("AboutDialog", "<ul>\n"
"<li>Floating IPS: <a href=\"https://www.smwcentral.net/?p=section&a=details&id=11474\" target=\"_blank\">https://www.smwcentral.net/?p=section&a=details&id=11474</a></li>\n"
"<li>PyQt5: <a href=\"https://www.riverbankcomputing.com/software/pyqt/intro\" target=\"_blank\">https://www.riverbankcomputing.com/software/pyqt/intro</a></li>\n"
"<li>Inno Setup: <a href=\"http://jrsoftware.org/isinfo.php\" target=\"_blank\">http://jrsoftware.org/isinfo.php</a></li>\n"
"</ul>"))
        self.label_6.setText(_translate("AboutDialog", "License"))
        self.label_8.setText(_translate("AboutDialog", "<p>Software is released under GNU General Public License.</p>\n"
"<ul>\n"
"<li>GNU GPL: <a href=\"https://www.gnu.org/licenses/gpl-3.0.en.html\" target=\"_blank\">https://www.gnu.org/licenses/gpl-3.0.en.html</a></li>\n"
"</ul>"))
        self.label_9.setText(_translate("AboutDialog", "<p>More details and source code available from the GitHub repository.</p>\n"
"<ul>\n"
"    <li>GitHub: <a href=\"https://github.com/smashedr/rom-patcher\" target=\"_blank\">https://github.com/smashedr/rom-patcher</a></li>\n"
"</ul>"))
        self.label_7.setText(_translate("AboutDialog", "Third Party Software"))

