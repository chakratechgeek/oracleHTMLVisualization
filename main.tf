"import requeired packages and class"
import urllib.request  as urllib2
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import xlsxwriter
from openpyxl.reader.excel import load_workbook
import env
import addmevent
import ioprofile
import sqlstats
import sgatarget

class Main:
    "This is main class for this application and whole program stats from here"

    def __init__ (self):
        "Constructor"

    def main (self):
        awrReportFile = str(input ("Enter the AWR report file name to be analyzed: "))

        try:
            fName = open (awrReportFile)
        except IOError:
            print ("Entered file is not accecible. Please entry correct AWR report.")
            exit ()
        finally:
            fName.close()

        htmlFile = open(awrReportFile, 'r', encoding='utf-8')
        sourceCode = htmlFile.read()
        soup = BeautifulSoup(sourceCode,"lxml")

        "Call DB, host and snap detail fetch class by defininig object"
        envDetail = env.Env()
        envDetail.extractenvinfo(soup)
        "Call ADDM and Foreground detail fetch class by defininig object"
        addmEventDetails = addmevent.AddmEvent()
        addmEventDetails.Addm(soup)
        "Call IO profile detail fetch class by defininig object"
        ioProfileDetails = ioprofile.IOProfile()
        ioProfileDetails.ioprofile(soup)
        "Call SQL Order by CPU detail fetch class by defininig object"
        cpuOrderByDetails = sqlstats.SqlStats()
        cpuOrderByDetails.sqlstatistics(soup)
        "Call SQL Order by Elapsed Time detail fetch class by defininig object"
        elapsedTimeOrderByDetails = sqlstats.SqlStats()
        elapsedTimeOrderByDetails.elapsedsqlstatistics(soup)
        "Call SQL Order by User IO detail fetch class by defininig object"
        userIOOrderByDetails = sqlstats.SqlStats()
        userIOOrderByDetails.iowaitsqlstatistics(soup)
        "Call SQL Order by Gets detail fetch class by defininig object"
        getsOrderByDetails = sqlstats.SqlStats()
        getsOrderByDetails.getssqlstatistics(soup)
        "Call SQL Order by Physical Reads detail fetch class by defininig object"
        pReadsOrderByDetails = sqlstats.SqlStats()
        pReadsOrderByDetails.preadssqlstatistics(soup)
        "Call SGA Target Advisory method to conclude"
        sgaTargetAdvise = sgatarget.SgaAdvisryTarget()
        sgaTargetAdvise.sgatargetadvisory(soup)

"Call main class and necessary functions"
fi = Main ()
fi.main()
