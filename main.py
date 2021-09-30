#!/usr/bin/python3
import tools, PIL
from PIL import Image, ImageColor

def userinput():
    data = eval(open('data.txt', 'r').read())
    data = tools.train(input('> '), data)
    datafile = open('data.txt', 'w')
    datafile.write(str(data))
    datafile.close()

def datainput(input_):
    data = eval(open('data.txt', 'r').read())
    data = tools.train(input_, data)
    datafile = open('data.txt', 'w')
    datafile.write(str(data))
    datafile.close()

def drive():
    data = eval(open('data.txt', 'r').read())
    starthex = tools.random.choice(list(data.keys()))
    hexlist = tools.drive(data, starthex)
    return hexlist

choice = input('User input (a) or data input (b) or drive (c): ')
if choice == 'a':
    userinput()
elif choice == 'b':
    datainput(input('Full file location please: '))
elif choice == 'c':
    output = input('What filename to save as?')
    hexlist = drive()
    print(len(hexlist))
    img = Image.frombytes(mode='P', size=(100,100), data=bytes(hexlist))
    img.save(output)