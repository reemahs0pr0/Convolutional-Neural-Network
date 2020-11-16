import xml.dom.minidom as xdm
import os
from PIL import Image
from numpy import asarray

def get_x_train():
    x_train = []
    for filename in os.listdir('data/train'):
        if not filename.endswith('.jpg'): 
            continue
        img_path_train = 'data/train/' + filename
        img = Image.open(img_path_train)
        img = img.convert('RGB').resize((32,32))
        data = asarray(img)
        x_train.append(data)
        for i in range(5):
            aug_img = img_aug(i, img)
            data = asarray(aug_img)
            x_train.append(data)
    return x_train

def get_x_test():
    x_test = []
    for filename in os.listdir('data/test'):
        if not filename.endswith('.jpg'): 
            continue
        img_path_train = 'data/test/' + filename
        img = Image.open(img_path_train)
        img = img.convert('RGB').resize((32,32))
        data = asarray(img)
        x_test.append(data)
    return x_test

def get_y_train():
    y_train = []
    for filename in os.listdir('data/train'):
        if not filename.endswith('.xml'): 
            continue
        path_train = 'data/train/' + filename
        doc = xdm.parse(path_train)
        name = doc.getElementsByTagName('name')
        if len(name) != 1:
            for i in range(len(name)):
                if i == len(name) - 1:
                    for i in range(6):
                        y_train.append(name[0].firstChild.data)
                    break
                if name[i].firstChild.data != name[i+1].firstChild.data:
                    for i in range(6):
                        y_train.append('mixed')
                    break
        else:
            for i in range(6):
                y_train.append(name[0].firstChild.data)
    return y_train

def get_y_test():
    y_test = []
    for filename in os.listdir('data/test'):
        if not filename.endswith('.xml'): 
            continue
        path_train = 'data/test/' + filename
        doc = xdm.parse(path_train)
        name = doc.getElementsByTagName('name')
        if len(name) != 1:
            for i in range(len(name)):
                if i == len(name) - 1:
                    y_test.append(name[0].firstChild.data)
                    break
                if name[i].firstChild.data != name[i+1].firstChild.data:
                    y_test.append('mixed')
                    break
        else:
            y_test.append(name[0].firstChild.data)
    return y_test

def img_aug(i, img):
    switcher = {
        0: img.transpose(Image.FLIP_LEFT_RIGHT),
        1: img.transpose(Image.FLIP_TOP_BOTTOM),
        2: img.rotate(90),
        3: img.rotate(180),
        4: img.rotate(270)
    }
    return switcher.get(i, None)