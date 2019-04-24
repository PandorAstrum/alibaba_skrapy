# -*- mode: python -*-
import gooey
gooey_root = os.path.dirname(gooey.__file__)
gooey_languages = Tree(os.path.join(gooey_root, 'languages'), prefix = 'gooey/languages')
gooey_images = Tree(os.path.join(gooey_root, 'images'), prefix = 'gooey/images')
block_cipher = None

added_files = [
            ('.\\alibaba', 'alibaba'),
            ('.\\scrapy.cfg', '.')
         ]

added_pathex = [
            'C:\\Users\\Ana Ash\\Desktop\\skrapy2\\vnv\\Scripts',
            'C:\\Users\\Ana Ash\\Desktop\\skrapy2\\project'
]

hidden_imported = [
            'bs4',
            'alibaba.spiders.alibaba_spiders'
]

added_binaries = [

    ]

options = [('u', None, 'OPTION'), ('u', None, 'OPTION'), ('u', None, 'OPTION')]

a = Analysis(['ui_support.py'],
             pathex=added_pathex,
             binaries=added_binaries,
             datas=added_files,
             hiddenimports=hidden_imported,
             hookspath=['.\\hooks\\'],
             runtime_hooks=None,
             #excludes=[],
             #win_no_prefer_redirects=False,
             #win_private_assemblies=False,
             #cipher=block_cipher,
             #noarchive=False
             )
pyz = PYZ(a.pure,
            # a.zipped_data,
            # cipher=block_cipher
            )
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          options,
          gooey_languages, # Add them in to collected files
          gooey_images, # Same here.
          name='Alibaba-Scrapper',
          debug=False,
         # bootloader_ignore_signals=False,
          strip=None,
          upx=True,
         # runtime_tmpdir=None,
          console=True )

# uncomment for a full app
#coll = COLLECT(exe,
    #a.binaries,
    #a.zipfiles,
    #a.datas,
    #options,
    #gooey_languages, # Add them in to collected files
    #gooey_images, # Same here.
    #name='BOT_Bot_GUI',
    #debug=False,
    #strip=False,
    #upx=True,
    #console=False,
    #windowed=True,
    #icon=os.path.join(gooey_root, 'images', 'program_icon.ico'))

