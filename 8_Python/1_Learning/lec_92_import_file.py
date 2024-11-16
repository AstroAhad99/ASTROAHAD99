# When we import the file like here we have imported lec_92_file_opera then it runs the file. This is also called
# absolute importing

from lec_92_file_opera import save_file, read_file
from lec_93_find import find_in

save_file("AHAD", 'C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\1_Learning\\lec_92_data.txt')
print(read_file('C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\1_Learning\\lec_92_data.txt'))

if __name__ == "__main__":
    getval = find_in(['Ahad', 'Ali', 'Ahmed'], lambda x:x, 'Some')
    print(getval)
    print(__name__)
# You can run this python file on bash using this command using the following command.
# python c:/Users/Qanare/Documents/ASTROAHAD99/8_Python/1_Learning/lec_92_import_file.py

