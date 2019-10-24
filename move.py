# /users/josh.flori/my/bin/python /users/josh.flori/documents/github/file_mover/move.py
import pandas as pd
from PIL import Image, ImageDraw, ImageFont



directory='/users/josh.flori/desktop'




# The purpose of this script 

events=pd.read_csv('/users/josh.flori/desktop/events.csv')
events['cumsum']=events['NUM_VISITOR_GROUPS'].cumsum()








img = Image.new('RGB', (1920,1080), color = (26, 26, 26))



# set font
fnt = ImageFont.truetype('/Library/Fonts/Verdana.ttf', 20)

d = ImageDraw.Draw(img)


x_start=100
x_end=1880
# these are inverse of what you expect
y_start=980
y_end=100

d.rectangle(((x_start, y_start), (x_end, y_end)))
d.rectangle(((x_start, y_end), (x_end, y_end)),outline=(26, 26, 26))
d.rectangle(((x_end, y_start), (x_end, y_end)),outline=(26, 26, 26))




# some measurements
n=4
t=events['TIME'][0]
n=events.shape[0]
length=x_end-x_start-10 # 10 is visual padding
height=y_start-y_end
ticks=[x_start+5]*num_tens
distance_per_tick=length/n
vertical_axis=list(range(events['cumsum'][n-1]+1))
vert_per_tick=height/vertical_axis[-1]

x="|"


pumpkin = Image.open("/users/josh.flori/desktop/pumpkin.png")



d.text((x_start+10,y_start-9), x, font=fnt1, fill=(255, 92, 57)) # 5 is padding, 9 is alignment
d.text((x_start-15,y_start+25), events['TIME'][0][0:4], font=fnt1, fill=(255, 92, 57))

for i in range(0,len(vertical_axis),5):
    q=25 if i<10 else 45
    d.text((x_start-q,y_start-(vert_per_tick*i)-30), str(vertical_axis[i]), font=fnt1, fill=(255, 92, 57))

img.save(directory+'/0.png')


for i in range(1,n):
    composite=Image.open(directory+'/'+str(i-1)+'.png')
    d = ImageDraw.Draw(composite)
    if i%10==0:
        d.text((x_start+10+(i*distance_per_tick),y_start-9), x, font=fnt1, fill=(255, 92, 57)) # 5 is padding, 9 is alignment
        d.text((x_start-15+(i*distance_per_tick),y_start+25), events['TIME'][i][0:4], font=fnt1, fill=(255, 92, 57))
        composite.save(directory+'/'+str(i)+'.png')
    else:
        d.text((x_start+10+(i*distance_per_tick),y_start-11), ".", font=fnt1, fill=(255, 92, 57))
        composite.paste(pumpkin, (x_start+10+(i*10), y_start-20-(11*events['cumsum'][i]))), pumpkin)
        composite.save(directory+'/'+str(i)+'.png')
    
    


