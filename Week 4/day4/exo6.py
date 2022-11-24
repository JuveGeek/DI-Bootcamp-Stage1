magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    print("Le nom de chaque magicien : ")
    for m in magicians:
        print(m)

def make_great(magic):
    for ma in range(0, int(len(magic))) :
        magic[ma]= magic[ma]+" "+"The great"
   

make_great(magician_names)


show_magicians(magician_names)