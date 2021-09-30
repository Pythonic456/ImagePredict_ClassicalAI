#!/usr/bin/python3
import string, random, PIL
from PIL import Image, ImageColor

def train(image, data):
    newdata = ''
    img_obj = Image.open(image)
    hexlist = []
    for hex in img_obj.getdata():
        hexlist.append(hex)
    for i in range(len(hexlist)):
        if i != len(hexlist)-1:
            if hexlist[i] in data:
                if hexlist[i+1] in data[hexlist[i]]:
                    data[hexlist[i]][hexlist[i+1]] += 1
                else: 
                    data[hexlist[i]][hexlist[i+1]] = 1
            else:
                data[hexlist[i]] = {hexlist[i+1]: 1}
    return data

def drive(data, starthex):
    hexlist = [starthex]
    for i in range(1, 100*100):
        try:
            chance = []
            for hex in data[hexlist[i-1]]:
                #print(data[hexlist[i-1]])
                for b in range(data[hexlist[i-1]][hex]):
                    chance.append(hex)
            hexlist.append(random.choice(chance))
        except:
            starthex = random.choice(list(data.keys()))
    return hexlist

