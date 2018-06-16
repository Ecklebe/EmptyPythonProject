# -*- mode: python -*-
import os
import sys

import markdown2
Path2Markdown2 = os.path.dirname(markdown2.__file__)

#import PyQt5
PathToPyQT5     = '' #os.path.dirname(PyQt5.__file__)
PathToPyQT5_bin = '' #os.path.join(PathToPyQT5, 'Qt\\bin')




block_cipher = None

added_files = [
         ( '..\\documentation\output', 'documentation\output' ),
		 ( '..\\CHANGELOG.md', '.' )
         ]
def Entrypoint(dist, group, name,
               scripts=None, 
			   pathex=None, 
			   binaries=None,
			   datas=None,
			   hiddenimports=None,
               hookspath=None, 
			   runtime_hooks=None,
			   excludes=None):
    import pkg_resources

    # get toplevel packages of distribution from metadata
    def get_toplevel(dist):
        distribution = pkg_resources.get_distribution(dist)
        if distribution.has_metadata('top_level.txt'):
            return list(distribution.get_metadata('top_level.txt').split())
        else:
            return []

    hiddenimports = hiddenimports or []
    packages = []
    for distribution in hiddenimports:
        packages += get_toplevel(distribution)

    scripts = scripts or []
    pathex = pathex or []
    # get the entry point
    ep = pkg_resources.get_entry_info(dist, group, name)
    # insert path of the egg at the verify front of the search path
    pathex = [ep.dist.location] + pathex
    # script name must not be a valid module name to avoid name clashes on import
    script_path = os.path.join(workpath, name + '-script.py')
    print ("creating script for entry point", dist, group, name)
    with open(script_path, 'w') as fh:
        print("import", ep.module_name, file=fh)
        print("%s.%s()" % (ep.module_name, '.'.join(ep.attrs)), file=fh)
        for package in packages:
            print ("import", package, file=fh)

    return Analysis([script_path] + scripts, pathex, binaries=binaries, datas=datas, hiddenimports=hiddenimports, hookspath=hookspath, runtime_hooks=runtime_hooks, excludes=excludes, win_no_prefer_redirects=False, win_private_assemblies=False, cipher=None)

a = Entrypoint('EmptyPythonProject', 'gui_scripts', 'EmptyPythonProject',
			scripts=['..//EmptyPythonProject//main.py'], 
            pathex=[PathToPyQT5_bin, Path2Markdown2],
            binaries=[],
            datas = added_files,
            hiddenimports=[],
            hookspath=[PathToPyQT5_bin],
            runtime_hooks=[],
            excludes=[])

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)


exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True)

		  