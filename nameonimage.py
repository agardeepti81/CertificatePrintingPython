import datetime
import sys
from PIL import Image, ImageDraw, ImageFont

    
if len(sys.argv)==1:
    name = str(input("Enter name: "))
    date = str(input("Enter Date: "))
elif len(sys.argv)==2:
    name = sys.argv[1]
    today = datetime.datetime.now()
    date = today.strftime("%m/%d/%Y")
elif len(sys.argv)>1 and len(sys.argv)<=3:
    name = sys.argv[1]
    date = sys.argv[2]

img = Image.open("\\deepti\\python\\CertficatePrinting\\certificate.jpeg")
print(img.size)
d = ImageDraw.Draw(img)
fnt = ImageFont.truetype("arial.ttf",50)
fntd = ImageFont.truetype("arialbd.ttf",25)
d.text((450,320),name.title(),font=fnt,fill=('#357E20'))
d.text((275,735),date,font=fntd,fill=('#357E20'))
img.save('\\deepti\\python\\CertficatePrinting\\certificate2.jpeg')
