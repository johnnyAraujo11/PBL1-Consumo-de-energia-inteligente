from datetime import time, datetime
import datetime as dt


h1= datetime.now()
h2 = time(17,00,50)
#print(h1.hour, h1.minute)


h3 = datetime.strptime("12", "%H")
h4 = datetime.strptime("15", "%H")
#print(str(h2.hour) - str(h1.hour))


d = dt.date.today()


print(type(str(d)))