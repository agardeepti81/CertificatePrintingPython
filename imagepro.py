import datetime, argparse
import sys
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser(description='print the certificate')
parser.add_argument("-first", type=str, help='Enter your first name: ')
parser.add_argument("-last", type=str, help='Enter your last name: ')
parser.add_argument("-date", type=str, help='Enter date of completion in mm/dd/yyyy format: ')
args = parser.parse_args()
first = args.first
last = args.last
date = args.date

if len(sys.argv)==4:
    first = sys.argv[1]
    last = sys.argv[2]
    date = sys.argv[3]
elif len(sys.argv)==3:
    first = sys.argv[1]
    last = sys.argv[2]
    today = datetime.datetime.now()
    date = today.strftime("%m/%d/%Y")
elif len(sys.argv)==2:
    first = sys.argv[1]
    last = str(input("Enter Last name: "))
    today = datetime.datetime.now()
    date = today.strftime("%m/%d/%Y")
elif len(sys.argv)==1:
    first = str(input("Enter first name: "))
    last = str(input("Enter Last name: "))
    today = datetime.datetime.now()
    date = today.strftime("%m/%d/%Y")


name = first+" "+last
img = Image.open("\\deepti\\python\\CertficatePrinting\\certificate.jpeg")
#print(img.size)
d = ImageDraw.Draw(img)
fnt = ImageFont.truetype("arial.ttf",50)
fntd = ImageFont.truetype("arialbd.ttf",25)
d.text((450,320),name.title(),font=fnt,fill=(0,0,0))
d.text((275,735),date,font=fntd,fill=(0,0,0))
img.save('\\deepti\\python\\CertficatePrinting\\certificate2.jpeg')



