
import os
from PIL import Image


images = list()
texts = list()
for root, dirs, files in os.walk("."):
    for filename in files:
        if 'txt' not in filename:
            images.append(filename)
        else:
            texts.append(filename)
                

                

text_numbers = list()
img_numbers = list()

for img in images:
        name = img.split('_')
        num_list = name[1].split('.')
        num = num_list[0]
        if num.isdigit():
            img_numbers.append(num)
            

for text in texts:
            tname = text.split('_')
            num_list = tname[1].split('.')
            number = num_list[0]
            if number.isdigit():
                text_numbers.append(number)
            
print('text length :' + str(len(text_numbers)))
print('image length :' + str(len(img_numbers)))
img_numbers.sort()
text_numbers.sort()
            
print('differences : ' + str(list(set(img_numbers) - set(text_numbers))))

        