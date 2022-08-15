import ftplib
from pathlib import Path
import rarfile

HOST = "138.201.56.185"
LOGIN = "rekrut"
PASSWORD = "zI4wG9yM5krQ3d"
directory = ''

downloadFolder = (Path.home() / "Desktop" / "task")
downloadFolder.mkdir(parents=True, exist_ok=True)

print('Folder\n', downloadFolder, '\n', '\t' * 4, '    was created\n')

ftp = ftplib.FTP(HOST,LOGIN, PASSWORD)


welcome = ftp.getwelcome()
print(welcome)

local_file= Path(downloadFolder,'copy_task.rar')#Ім'я створюваного локального файл
download= 'task.rar'

with open(local_file,'wb') as file: #Створюємо локальний файл в режимі двоїчного запису
    ftp.retrbinary('RETR %s' % download, file.write, )#Відкриваємо файл на сервері і робимо його копію в локальний файл
print('File downloaded')
ftp.close()
print("ftp.close()")


rarfile.RarFile(local_file).extractall(Path(downloadFolder, 'UnRAR'))
print('UnRARed')

ftp = ftplib.FTP(HOST,LOGIN, PASSWORD)

paths = sorted(Path(downloadFolder, 'UnRAR').glob('*.*'))

print(ftp.pwd())
ftp.cwd('/complete/Roman/')
print(ftp.pwd())

for f in paths:
    with open(f, 'rb') as file:
        ftp.storbinary('STOR ' + str(f.name), file)

    
print("END")
ftp.close()

