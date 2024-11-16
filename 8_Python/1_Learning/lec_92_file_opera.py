def save_file(content, file):
    with open(file,'w') as savefile:
        savefile.write(content)


def read_file(file):
    with open(file, 'r') as readfile:
        return readfile.read()
    

print(__name__)