# -*- mode: python -*-

block_cipher = None

added_files = [
         ( '..\\documentation\output', 'documentation\output' ),
		 ( '..\\CHANGELOG.md', '.' )
         ]

a = Analysis(['..\\code\\main.py'],
             pathex=[],
             binaries=[],
             datas = added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)


exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='EmptyPythonProject',
          debug=False,
          strip=False,
          upx=True,
          console=False )
		  