from PIL import Image, ImageDraw, ImageFont
import sys,os
import datetime


class CertificatePrintingEngine:
    def __init(self):    
        pass
    
    def Print(self,name, date, outFile):
        img = Image.open(self.inFile)
        d = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(self.tFont,self.sizeText)
        fntd = ImageFont.truetype(self.dFont,self.sizeDate)
        d.text((self.xtext,self.ytext),name,font=fnt,fill=(self.RED,self.GREEN,self.BLUE))
        d.text((self.xdate,self.ydate),date,font=fntd,fill=(self.RED,self.GREEN,self.BLUE))
        img.save(outFile)
    
    def setInputFile(self, inFile):
        self.inFile = inFile
    
    def setTextColor(self,RED,GREEN,BLUE):
        self.RED = RED
        self.GREEN = GREEN
        self.BLUE = BLUE
        return self.RED, self.GREEN, self.BLUE

    def setTextPosition(self, xtext, ytext):
        self.xtext = xtext
        self.ytext = ytext
        
    def setDatePosition(self, xdate, ydate):
        self.xdate = xdate
        self.ydate = ydate
        
    def setTextFont(self, tFont,sizeText):
        self.tFont = tFont
        self.sizeText = sizeText
        
    def setDateFont(self,dFont, sizeDate):
        self.dFont = dFont
        self.sizeDate = sizeDate
        
    def setName(self, first, last):
        self.first = first
        self.last = last
        name = first +" "+last
        return ( name.title())

    def setOutputFile(self, name):
        self.name = name
        os.chdir('C:\Deepti\Python\CertficatePrinting\output')
        OutFile = self.name+"_Ceritificate.jpeg"
        return OutFile
             
