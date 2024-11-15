"""

For this program we will have the input of 3 friends and it will look into the people.txt file that if the those 3 friends input exist or not

"""

friends = input("Enter the names of 3 friends without spaces (only add commas): ")

people = open("C:\\Users\\aahad\\Documents\\AhadVS\\ASTROAHAD99\\8_Python\\1_Learning\\lec_85_people.txt", "r")
#people_nearby = people.readlines()
people_nearby = [line.strip() for line in people.readlines()]
people.close()


people_set = set(people_nearby)
friends_set = set(friends)
friends_nearby = friends_set.intersection(friends_set)

nearby_friends_file = open("C:\\Users\\aahad\\Documents\\AhadVS\\ASTROAHAD99\\8_Python\\1_Learning\\lec_85_nearby_friends.txt", "w")

for friend in friends_nearby:
    nearby_friends_file.write(f"{friend}")

nearby_friends_file.close()