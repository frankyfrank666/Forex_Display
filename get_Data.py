import datetime
import pandas_datareader as web 

def get_Data():
    start = datetime.datetime(2018, 1, 2)
    SGDCNY = web.DataReader('SGDCNY=X','yahoo',start) 
    SGDMYR = web.DataReader('SGDMYR=X','yahoo',start)
    SGDUSD = web.DataReader('SGD=X','yahoo',start)

    return [SGDCNY,SGDMYR,SGDUSD]