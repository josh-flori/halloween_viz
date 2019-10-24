# /users/josh.flori/my/bin/python /users/josh.flori/documents/github/file_mover/move.py
import pandas as pd
from PIL import Image, ImageDraw, ImageFont



directory='/users/josh.flori/desktop'




# The purpose of this script 

events=pd.read_csv('/users/josh.flori/desktop/events.csv')
events['cumsum']=events['NUM_VISITOR_GROUPS'].cumsum()








img = Image.new('RGB', (1920,1080), color = (26, 26, 26))



# set font
fnt = ImageFont.truetype('/Library/Fonts/Verdana.ttf', 30)

d = ImageDraw.Draw(img)

d.rectangle(((100, 980), (1880, 100)))
d.rectangle(((100, 100), (1880, 100)),outline=(26, 26, 26))
d.rectangle(((1880, 980), (1880, 100)),outline=(26, 26, 26))


# add user
n=4
x=events['TIME'][0]
x="|"
d.text((100,505), x, font=fnt1, fill=(42, 175, 247))
d.text((115,505), ".", font=fnt1, fill=(42, 175, 247))
d.text((140,505), ".", font=fnt1, fill=(42, 175, 247))
d.text((160,505), ".", font=fnt1, fill=(42, 175, 247))
d.text((180,505), ".", font=fnt1, fill=(42, 175, 247))
d.text((200,505), ".", font=fnt1, fill=(42, 175, 247))

i=1
img.save(directory+'/'+str(i)+'.png')


num_lines=events.shape[0]
for i in range(num_lines):
    