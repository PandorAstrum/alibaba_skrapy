# -*- mode: python -*-

block_cipher = None

added_files = [
            ('alibaba', 'alibaba'),
         ]

added_pathex = [
            'C:\\Users\\Ana Ash\\Desktop\\skrapy2\\project'
        ]

hidden_imported = [
            'bs4'
        ]

added_binaries = [

    ]


a = Analysis(['ui.py'],
             pathex=added_pathex,
             binaries=added_binaries,
             datas=added_files,
             hiddenimports=hidden_imported,
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
          [],
          exclude_binaries=True,
          name='Alibaba-Scrapper',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Alibaba-Scrapper')