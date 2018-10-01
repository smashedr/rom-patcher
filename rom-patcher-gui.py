import os
import re
import requests
import sys
import subprocess
import tempfile
import traceback
import zipfile
from bs4 import BeautifulSoup
from configparser import ConfigParser
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from gui.main import Ui_MainWindow
from gui.about import Ui_AboutDialog
from gui.help import Ui_HelpDialog


class WinMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setWindowIcon(QtGui.QIcon(resource_path(icon_file)))
        self.setupUi(self)
        self.results_box.setText('Welcome to ROM Patcher.')
        self.config_file = os.path.abspath('settings.ini')
        self.config = self.setup_config()
        self.results_box.setReadOnly(True)
        self.input_select.clicked.connect(self.open_input)
        self.file_input_select.triggered.connect(self.open_input)
        self.source_select.clicked.connect(self.open_source)
        self.file_source_select.triggered.connect(self.open_source)
        self.output_select.clicked.connect(self.open_output)
        self.file_output_select.triggered.connect(self.open_output)
        self.file_save_settings.triggered.connect(self.save_settings)
        self.file_exit_app.triggered.connect(self.close)
        self.help_about.triggered.connect(self.show_about)
        self.help_help.triggered.connect(self.show_help)
        self.patch_button.clicked.connect(self.patch_rom)
        self.source_open.clicked.connect(self.open_source_dir)
        self.output_open.clicked.connect(self.open_output_dir)
        self.rom_open.clicked.connect(self.open_rom_dir)
        self.exit_app.clicked.connect(self.close)

    def save_settings(self):
        self.update_config()
        self.results_box.setText('Source ROM and Output Directory saved.\n\n'
                                 'Note: Your settings are saved automatically '
                                 'every time you patch a rom successfully...')

    def show_about(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_AboutDialog()
        dialog.ui.setupUi(dialog)
        dialog.setWindowIcon(QtGui.QIcon(resource_path(icon_file)))
        dialog.exec_()
        dialog.show()

    def show_help(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_HelpDialog()
        dialog.ui.setupUi(dialog)
        dialog.setWindowIcon(QtGui.QIcon(resource_path(icon_file)))
        dialog.exec_()
        dialog.show()

    def setup_config(self):
        config = ConfigParser()
        if os.path.isfile(self.config_file):
            config.read(self.config_file)
        if 'main' in config:
            if 'smw_rom' in config['main']:
                self.source_rom.setText(config['main']['smw_rom'])
            if 'out_dir' in config['main']:
                self.output_dir.setText(config['main']['out_dir'])
        else:
            try:
                config.add_section('main')
                config.write(open(self.config_file, 'w'))
            except:
                pass
        QtWidgets.qApp.processEvents()
        return config

    def update_config(self):
        self.config.set('main', 'smw_rom', self.source_rom.text())
        self.config.set('main', 'out_dir', self.output_dir.text())
        try:
            self.config.write(open(self.config_file, 'w'))
        except:
            pass

    def open_rom_dir(self):
        target = self.results_box.toPlainText()
        if os.path.isfile(target):
            open_file_loc(target)
        else:
            self.results_box.setText('Unable to locate finished ROM file...')

    def open_source_dir(self):
        open_file_loc(self.source_rom.text())

    def open_output_dir(self):
        open_dir_loc(self.output_dir.text())

    def patch_rom(self):
        self.results_box.setText('ROM Patcher is working, please wait...')
        QtWidgets.qApp.processEvents()
        if self.input_patch.text() and \
                self.source_rom.text() and \
                self.output_dir.text():

            rom = RomPatcher(
                self.input_patch.text(),
                self.source_rom.text(),
                self.output_dir.text(),
            )
            self.update_config()
            self.results_box.setText(rom.message)
        else:
            self.results_box.setText('Please fill out all 3 fields above...')

    def open_input(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        patch_file, _ = QFileDialog.getOpenFileName(
            self, 'ROM Patch File', '',
            'Patch Files (*.ips *.bps *.zip);;All Files (*)',
            options=options
        )
        if patch_file:
            if os.path.isfile(patch_file):
                self.input_patch.setText(patch_file)
                self.results_box.setText('Patch File selected OK.')
            else:
                self.results_box.setText('Error: Patch File appears to be invalid.')

    def open_source(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        patch_file, _ = QFileDialog.getOpenFileName(
            self, 'Source ROM File', '',
            'Patch Files (*.smc *.sfc);;All Files (*)',
            options=options
        )
        if patch_file:
            if os.path.isfile(patch_file):
                self.source_rom.setText(patch_file)
                self.results_box.setText('Source ROM selected OK.')
            else:
                self.results_box.setText('Error: Source ROM appears to be invalid.')

    def open_output(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        out_dir = str(QFileDialog.getExistingDirectory(self, 'Select Directory'))
        if out_dir:
            if os.path.isdir(out_dir):
                self.output_dir.setText(out_dir)
                self.results_box.setText('Output Directory selected OK.')
            else:
                self.results_box.setText('Error: Output Directory appears to be invalid.')


class RomPatcher(object):
    def __init__(self, patch, source, destination):
        self.patch = patch
        self.source = source
        self.destination = destination
        self.success = False
        self.message = None
        self.rom = None
        self.apply_patch()

    def __repr__(self):
        return self.rom if self.rom else 'RomPatcher Class: None'

    def apply_patch(self):
        try:
            patch_pattern = '\.(bps|ips)$'
            zip_pattern = '\.(zip)$'

            tmpdir = tempfile.TemporaryDirectory()
            temp_dir = tmpdir.name

            if not os.path.isfile(self.patch):
                rom_url = self.patch
                if not re.search(zip_pattern, self.patch, re.IGNORECASE) and \
                        not re.search(patch_pattern, self.patch, re.IGNORECASE):
                    r = requests.get(self.patch, verify=False)
                    if r.status_code != 200:
                        msg = ('Error retrieving remote resource.\n '
                               'Remote server response code: '
                               '{}'.format(r.status_code))
                        return self._fail(msg)
                    soup = BeautifulSoup(r.content.decode(), 'html.parser')
                    download = soup.find(string='Download')
                    rom_uri = download.findPrevious()['href']
                    if not rom_uri:
                        msg = ('Unable to locate a ROM download at the '
                               'provided url: {}'.format(self.patch))
                        return self._fail(msg)
                    rom_url = 'https:{}'.format(rom_uri)

                r = requests.get(rom_url, verify=False)
                if r.status_code != 200:
                    msg = 'Error retrieving resource: {}'.format(r.status_code)
                    return self._fail(msg)

                file_path = os.path.join(temp_dir, os.path.basename(rom_url))
                with open(file_path, 'wb') as f:
                    f.write(r.content)
                    f.close()
            else:
                file_path = os.path.abspath(self.patch)

            if re.search(zip_pattern, file_path, re.IGNORECASE):
                archive = zipfile.ZipFile(file_path)
                archive.extractall(temp_dir)
                archive.close()
                patch_file = self.find_first_file(temp_dir, patch_pattern)
            else:
                patch_file = file_path

            # patch_path = os.path.join(temp_dir, patch_file)
            patch_name = re.split(patch_pattern, patch_file)[0]
            self.rom = os.path.join(self.destination, '{}.sfc'.format(
                os.path.basename(patch_name)
            ))

            cmd_l = [
                os.path.join(bin_dir, flips), '--apply', '--exact',
                patch_file, self.source, self.rom,
            ]
            subprocess.check_call(cmd_l, startupinfo=startupinfo)
            tmpdir.cleanup()
            self.success = True
            self.message = self.rom
        except:
            return self._fail(traceback.format_exc())

    @staticmethod
    def find_first_file(directory, pattern):
        for root, subdirs, files in os.walk(directory):
            for f in files:
                if re.search(pattern, f):
                    return os.path.join(root, f)

    def _fail(self, message):
        self.message = message
        self.success = False
        return False


def open_dir_loc(directory):
    if sys.platform == 'win32':
        target = directory.replace('/', '\\')
        command = 'explorer.exe /root,"{}\\"'.format(target)
    else:
        command = ['xdg-open', directory]
    subprocess.call(command)


def open_file_loc(directory):
    if sys.platform == 'win32':
        target = directory.replace('/', '\\')
        command = 'explorer.exe /select,"{}"'.format(target)
    else:
        command = ['xdg-open', os.path.dirname(directory)]
    subprocess.call(command)


def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.abspath(os.path.join(sys._MEIPASS, relative))
    return os.path.abspath(os.path.join(relative))


if __name__ == '__main__':
    startupinfo = None
    if sys.platform == 'win32':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    flips = 'flips.exe' if sys.platform == 'win32' else 'flips-linux'
    # icon_file = 'icon.icns' if sys.platform == 'darwin' else 'icon.ico'
    icon_file = 'icon.ico'
    bin_dir = resource_path('bin')

    app = QApplication(sys.argv)
    window = WinMain()
    window.show()
    sys.exit(app.exec_())
