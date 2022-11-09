# WAP for zipping and unzipping files.

from zipfile import ZipFile
zf = ZipFile('SEM-2\\Advanced Python Programming\\practical-1\\file.zip', 'r')

zf.extractall('SEM-2/Advanced Python Programming/practical-1/extracted')
zf.close()