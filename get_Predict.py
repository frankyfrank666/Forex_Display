import datetime
import pandas as pd
from prophet import Prophet
import get_Data
import Plot
import Period
import matplotlib.pyplot as plt

[SGDCNY,SGDMYR,SGDUSD] = get_Data.get_Data()
end = datetime.date.today() - datetime.timedelta(weeks=26)

def get_Predict(SGDCNY,SGDMYR,SGDUSD,periods=365):

    SGDCNY = SGDCNY['High']/2+SGDCNY['Low']/2
    SGDMYR = SGDMYR['High']/2+SGDMYR['Low']/2
    SGDUSD = SGDUSD['High']/2+SGDUSD['Low']/2

    m = Prophet()
    m.fit(SGDCNY)
    SGDCNYfuture = m.make_future_dataframe(periods=periods)

    m = Prophet()
    m.fit(SGDMYR)
    SGDMYRfuture = m.make_future_dataframe(periods=periods)

    m = Prophet()
    m.fit(SGDUSD)
    SGDUSDfuture = m.make_future_dataframe(periods=periods)

    return [SGDCNYfuture,SGDMYRfuture,SGDUSDfuture]

new_start = Period.change_Time('MX')

fig, ax1, ax2, ax3 = Plot.plot(SGDCNY,SGDMYR,SGDUSD,new_start,1,0,end)
[SGDCNYfuture,SGDMYRfuture,SGDUSDfuture] = get_Predict(SGDCNY,SGDMYR,SGDUSD,365//2)

print(SGDCNYfuture.head())