import smtplib

import pandas
from datetime import datetime

today_month = datetime.now().month
today_date = datetime.now().day
data = pandas.read_csv('data.csv')
month = data.month.to_list()
my_mail = "shreekantpukale16@gmail.com"
password = "Thisshouldcontainyourpassword"
if today_month in month:
    row_data = data[data.month == today_month]
    if int(today_date) == int(row_data.date):
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs=row_data.gmail, msg=f"SUBJECT: HAPPY BIRTHDAY\n\n"
                                                                           f"Have a lot of cake but don't be diabetic "
                                                                           f"From your loving Shreekant")
        connection.close()
