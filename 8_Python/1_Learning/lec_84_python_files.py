my_file = open('C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\1_Learning\\lec_84_data.txt', 'r')
my_content = my_file.read()
my_file.close()

print(my_content)

user_name = input('Enter name: ')

my_file2 = open('C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\1_Learning\\lec_84_data.txt', 'w')
my_file2.write(user_name)
my_file2.close()