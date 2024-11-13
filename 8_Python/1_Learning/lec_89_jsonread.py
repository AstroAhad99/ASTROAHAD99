import json

file = open("C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\1_Learning\\lec_89_json_file.txt", 'r')
file_contents = json.load(file) #read the file and convert it to dictionary
file.close()

print(file_contents['friends'][0])

# json.dump is to save the data in txt file
# json.load is to load json file

my_data = [
    {
        'name':'Ahad',
        'degree':'Engineering'
    },
    {
        'name':'Ali',
        'degree':'MBBS'
    }
]

open_again = open("C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\1_Learning\\lec_89_json_file.txt", 'w')

json.dump(my_data, open_again)

