from PIL import Image
import matplotlib.pyplot as plt

# def img_aug(i, img):
#     switcher = {
#         0: img.transpose(Image.FLIP_LEFT_RIGHT),
#         1: img.rotate(45),
#         2: img.rotate(90),
#         3: img.rotate(-45),
#         4: img.rotate(-90),
#     }
#     return switcher.get(i, None)

# img = Image.open('data/train/banana_51.jpg')
# img = img.convert('RGB').resize((64,64))
# plt.imshow(img)
# plt.show()
# for i in range(5):
#     aug_img = img_aug(i, img)
#     plt.imshow(aug_img)
#     plt.show()

import xml.dom.minidom as xdm
import os

for filename in os.listdir('data/test'):
    # if filename.startswith('mixed'):      
        if filename.endswith('.jpg'): 
            img_path_train = 'data/test/' + filename
            img = Image.open(img_path_train)
            img = img.convert('RGB').resize((128,128))
            plt.imshow(img)
            plt.show()
        elif filename.endswith('.xml'): 
            path_train = 'data/test/' + filename
            doc = xdm.parse(path_train)
            name = doc.getElementsByTagName('name')
            if len(name) != 1:
                for i in range(len(name)):
                    if i == len(name) - 1:
                        print(filename)
                        print(name[0].firstChild.data)
                        break
                    if name[i].firstChild.data != name[i+1].firstChild.data:
                        print(filename)
                        print('mixed')
                        break
            else:
                print(filename)
                print(name[0].firstChild.data)