my_ques = open("C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\2_Challenge\\read_write_file.txt", "r")

get_ques = [ques.strip() for ques in my_ques.readlines()]
my_ques.close()

ques_only = []

num_ques = len(get_ques)

for string in get_ques:
    ques_only.append(string.rsplit("="))

correct = 0

for ques in ques_only:
    ask = input(f"Question: {ques[0]} = ")
    if ask == ques[1]:
        correct+=1

print(f"Your final score is {correct}/{num_ques}.")
