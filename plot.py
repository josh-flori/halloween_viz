# Cumulative trick-or-treater visits 


import pandas as pd
from PIL import Image, ImageDraw, ImageFont




import wave
from os import path
from pydub import AudioSegment
from pydub import AudioSegment
from pydub.playback import play
from moviepy.editor import *
import numpy as np
import itertools





directory='/users/josh.flori/desktop'




# The purpose of this script 

events=pd.read_csv('/users/josh.flori/desktop/events.csv')
events['cumsum']=events['groups'].cumsum()








img = Image.new('RGB', (1920,1080), color = (26, 26, 26))



# set font
fnt1 = ImageFont.truetype('/Library/Fonts/Verdana.ttf', 40)
fnt2 = ImageFont.truetype('/Library/Fonts/Verdana.ttf', 35)
fnt3 = ImageFont.truetype('/Library/Fonts/Verdana.ttf', 25)


d = ImageDraw.Draw(img)


x_start=100
x_end=1800
# these are inverse of what you expect
y_start=980
y_end=240



d.rectangle(((x_start, y_start), (x_end, y_end-70)))
d.rectangle(((x_start, y_end-70), (x_end, y_end-70)),outline=(26, 26, 26))
d.rectangle(((x_end, y_start), (x_end, y_end-70)),outline=(26, 26, 26))




# some measurements
n=events.shape[0]
length=x_end-x_start-10 # 10 is visual padding
height=y_start-y_end
distance_per_tick=length/n
vertical_axis=list(range(events['cumsum'][n-1]+2))
vert_per_tick=height/vertical_axis[-1]

x="|"


pumpkin = Image.open("/users/josh.flori/desktop/pumpkin.png")
title=Image.open('/users/josh.flori/desktop/title.png')



d.text((x_start+10,y_start-9), x, font=fnt1, fill=(255, 92, 57)) # 5 is padding, 9 is alignment
d.text((x_start-15,y_start+40), events['TIME'][0][0:4], font=fnt2, fill=(255, 92, 57))

# AXIS LABELS
d.text((x_start-70,30), "Total Trick\n   - or - \n Treaters", font=fnt3, fill=(200, 200, 200))
d.text((1840,1020), "PM", font=fnt2, fill=(200, 200, 200))


for i in range(0,len(vertical_axis),5):
    q=45 if i<10 else 65
    d.text((x_start-q,y_start-(vert_per_tick*i)-65), str(vertical_axis[i]), font=fnt1, fill=(255, 92, 57))

img.save(directory+'/0.png')
composite=Image.open(directory+'/0.png')
composite.paste(title, (600, 10), title)
composite.save(directory+'/0.png')


for i in range(1,n):
    composite=Image.open(directory+'/'+str(i-1)+'.png')
    d = ImageDraw.Draw(composite)
    if i%10==0:
        d.text((x_start+10+(i*distance_per_tick),y_start-9), x, font=fnt1, fill=(255, 92, 57)) # 5 is padding, 9 is alignment
        d.text((x_start-17+(i*distance_per_tick),y_start+40), events['TIME'][i][0:4], font=fnt2, fill=(255, 92, 57))
        if events['cumsum'][i-1] != events['cumsum'][i]:
            composite.paste(pumpkin, (x_start+(i*int(distance_per_tick)), y_start-60-(int(vert_per_tick)*events['cumsum'][i])), pumpkin)
        composite.save(directory+'/'+str(i)+'.png')
    else:
        d.text((x_start+10+(i*distance_per_tick),y_start-11), ".", font=fnt1, fill=(255, 92, 57))
        if events['cumsum'][i-1] != events['cumsum'][i]:
            composite.paste(pumpkin, (x_start+(i*int(distance_per_tick)), y_start-60-(int(vert_per_tick)*events['cumsum'][i])), pumpkin)
            composite.save(directory+'/'+str(i)+'.png')
        else:
            composite.save(directory+'/'+str(i)+'.png')

    

clips = [ImageClip(directory+'/'+str(i)+".png").set_duration(.05) if i != n-1 else ImageClip(directory+'/'+str(i)+".png").set_duration(1.3) for i in range(n)] # <-- give the last frame a little time to breath before jumping into the next 


concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile(directory+"/spooky.mp4", fps=30)









bar=pd.read_csv('/users/josh.flori/desktop/bar.csv')







x_start=100
x_end=1830
# these are inverse of what you expect
y_start=980
y_end=150

# some measurements
n=bar.shape[0]
length=x_end-x_start-10 # 10 is visual padding
height=y_start-y_end
distance_per_tick=length/n
vertical_axis=list(range(bar['count'].max()+1))
vert_per_tick=height/vertical_axis[-1]

x="|"





img = Image.new('RGB', (1920,1080), color = (26, 26, 26))
d = ImageDraw.Draw(img)

d.rectangle(((x_start, y_start), (x_end, y_end)))
d.rectangle(((x_start, y_end), (x_end, y_end)),outline=(26, 26, 26))
d.rectangle(((x_end, y_start), (x_end, y_end)),outline=(26, 26, 26))

d.text((x_start+10,y_start-9), x, font=fnt1, fill=(255, 92, 57)) # 5 is padding, 9 is alignment
d.text((x_start-15,y_start+40), bar['5_min'][0][0:4], font=fnt2, fill=(255, 92, 57))

# AXIS LABELS
d.text((x_start-70,22), "Total Trick\n   - or - \n Treaters", font=fnt3, fill=(200, 200, 200))
d.text((1840,1020), "PM", font=fnt2, fill=(200, 200, 200))

for i in range(1,len(vertical_axis)):
    d.text((x_start-39,y_start-(vert_per_tick*i)), str(vertical_axis[i]), font=fnt1, fill=(255, 92, 57))

img.save(directory+'/0.png')
composite=Image.open(directory+'/0.png')
composite.paste(title, (600, 10), title)
composite.save(directory+'/0.png')






for i in range(1,n):
    composite=Image.open(directory+'/'+str(i-1)+'.png')
    d = ImageDraw.Draw(composite)
    if i%2==0:
        d.text((x_start+8+(i*distance_per_tick),y_start-9), x, font=fnt1, fill=(255, 92, 57)) # 5 is padding, 9 is alignment
        d.text((x_start-17+(i*distance_per_tick),y_start+40), bar['5_min'][i][0:4], font=fnt2, fill=(255, 92, 57))
        if bar['count'][i] >0:
            for h in range(1,bar['count'][i]+1):
                composite.paste(pumpkin, (x_start+(i*int(distance_per_tick)), y_start-35-(int(vert_per_tick-2)*h)), pumpkin)
        composite.save(directory+'/'+str(i)+'.png')
    else:
        d.text((x_start+8+(i*distance_per_tick),y_start-9), ".", font=fnt1, fill=(255, 92, 57))
        if bar['count'][i] >0:
            for h in range(1,bar['count'][i]+1):
                composite.paste(pumpkin, (x_start+(i*int(distance_per_tick)), y_start-35-(int(vert_per_tick-2)*h)), pumpkin)
            composite.save(directory+'/'+str(i)+'.png')    
        else:
            composite.save(directory+'/'+str(i)+'.png')
        
clips = [ImageClip(directory+'/'+str(i)+".png").set_duration(.3) if i != n-1 else ImageClip(directory+'/'+str(i)+".png").set_duration(1.3) for i in range(n)] # <-- give the last frame a little time to breath before jumping into the next 


concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile(directory+"/spooky1.mp4", fps=30)
