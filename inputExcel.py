import sys, datetime
import pandas as pd
from certEngine import CertificatePrintingEngine

cpe = CertificatePrintingEngine()

class getDatafromExcel:
    def __init(self):    
        pass
        
    def getRow(self, df):
        for row in df.itertuples(index = False):
            name = cpe.setName(row.first,row.last)
            if(pd.isnull(row.date)):
                today = datetime.datetime.now()
                date = today.strftime("%Y-%m-%d") 
            else:
                date = pd.Timestamp.date(row.date)
            
            cpe.setInputFile(row.inFile)
            cpe.setTextColor(row.RED,row.GREEN,row.BLUE)
            cpe.setTextFont(row.tFont,row.sizeText)
            cpe.setTextPosition(row.xtext,row.ytext)
            cpe.setDatePosition(row.xdate,row.ydate)
            cpe.setDateFont(row.dFont,row.sizeDate)
            outFile = cpe.setOutputFile(name)
            cpe.Print(name,str(date),outFile)
            
            
        
        
