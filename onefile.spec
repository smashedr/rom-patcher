# -*- mode: python -*-

block_cipher = None


a = Analysis(['rom-patcher-gui.py'],
             binaries=[],
             datas=[('assets/icon.ico', '.'), ('settings.ini', '.')],
             hiddenimports = [],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          Tree('bin', prefix='bin'),
          a.zipfiles,
          a.datas,
          [],
          name='rom-patcher',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='assets/icon.ico')
