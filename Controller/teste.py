from datetime import datetime, timedelta
current = datetime.now()
#print("This is the current date and time :- ", current)
 
tomorrow = timedelta(1)
#print("Tomorrow's date and time :- ", current + tomorrow)
 
yesterday = timedelta(-1)
#print("Yesterday's date and time :- ", current + yesterday)

date_i = datetime.strptime('12/04/2023 12:00', '%d/%m/%Y %H:%M')
date_f = datetime.strptime('12/03/2023 12:00', '%d/%m/%Y %H:%M')

new_date = date_i + timedelta(30)
print(type(date_i))