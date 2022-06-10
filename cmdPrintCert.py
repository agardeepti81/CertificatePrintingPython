from certEngine import CertificatePrintingEngine
from certArg import CertificatePrinterArguments 

cpe = CertificatePrintingEngine()
cpargs = CertificatePrinterArguments()
cpe.setInputFile(cpargs.inFile)
cpe.setTextColor(cpargs.RED,cpargs.GREEN,cpargs.BLUE)
cpe.setTextFont(cpargs.tFont,cpargs.sizeText)
cpe.setTextPosition(cpargs.xtext,cpargs.ytext)
cpe.setDatePosition(cpargs.xdate,cpargs.ydate)
cpe.setDateFont(cpargs.dFont,cpargs.sizeDate)
cpe.Print(cpargs.Name(),cpargs.date,cpargs.OutputFile() )

