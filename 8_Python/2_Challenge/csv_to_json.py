# Strip and Split are the two important function which are used to convert the data in , comma seperated to 
# json format

import json

json_list = []      # store the converted json data for each line

with open('C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\2_Challenge\\csv_to_json_load.txt','r') as file:
    for line in file.readlines():
        club, city, country = line.strip().split(',')   # first get rid of the \n and then split with ','
        data = {
            'club': club,
            'city': city,
            'country': country
        }
        json_list.append(data)

#csv_file = open('C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\2_Challenge\\csv_to_json_load.txt', 'r')
 
# for line in csv_file.readlines():
#     club, city, country = line.strip().split(',')   # first get rid of the \n and then split with ','
#     data = {
#         'club': club,
#         'city': city,
#         'country': country
#     }
#     json_list.append(data)
 
#csv_file.close()
 
#json_file = open('C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\2_Challenge\\csv_to_json_dump.txt', 'w')
#json.dump(json_list, json_file)     # write json data to a file
#json_file.close()

with open('C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\2_Challenge\\csv_to_json_dump.txt','w') as json_file:
    json.dump(json_list, json_file)

