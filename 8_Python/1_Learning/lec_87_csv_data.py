file = open("C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\1_Learning\\lec_87_csv_data.txt", 'r')
lines = file.readlines()
file.close()

in_list_lines = [line.strip() for line in lines]

for line in in_list_lines:
    person_data = line.split(',')
    name = person_data[0]
    age = person_data[1]
    uni = person_data[2]
    degree = person_data[3]

    print(f"{name.title()} is {age} years old, studying {degree.title()} in {uni.upper()} university.")

sample_csv = ','.join(['Ahad','25','UIT','Automation'])
print(sample_csv)