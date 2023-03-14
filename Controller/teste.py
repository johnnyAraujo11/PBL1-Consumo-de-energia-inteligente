from datetime import datetime

# current date and time
now = datetime.now()


s1 = now.strftime("%m/%d/%Y")



data_ = '01/03/2018 12:00'
data2 = '01/03/2018 12:05'

dh = datetime.strptime(data_, '%d/%m/%Y %H:%M')
dh2 = datetime.strptime(data2, '%d/%m/%Y %H:%M')


print(dh < dh2)
