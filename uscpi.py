import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start_date = '2020-01-01'
end_date = datetime.date.today()

cpi_data = web.DataReader(["CPIAUCSL"], 'fred', start_date, end_date)
df_cpi_us = cpi_data.pct_change(12)*100
plt.plot(df_cpi_us.index, df_cpi_us)
plt.xlabel('Date')
plt.ylabel('CPI MoM Change (%)')
plt.show()