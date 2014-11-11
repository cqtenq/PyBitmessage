# -*- mode: python -*-
a = Analysis(['src\\bitmessagemain.py'],
             pathex=['D:\\FTC\\dev\\PyInstaller-2.1\\bitmessagemain'],
             hiddenimports=[],
             hookspath=None)
			 
def addTranslations():
    import os
    extraDatas = []
    for file in os.listdir('src\\translations'):
        extraDatas.append(('translations\\'+file, 'src\\translations\\' + file, 'DATA'))
    return extraDatas

# append the translations directory
a.datas += addTranslations()
			 
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          a.binaries + [('libeay32.dll', 'c:\\OpenSSL-Win32\\bin\\libeay32.dll', 'BINARY')],
          name=os.path.join('dist', 'bitmessagemain.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='src\\images\\can-icon.ico')
app = BUNDLE(exe,
             name=os.path.join('dist', 'bitmessagemain.exe.app'))