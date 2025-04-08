from datetime import *
d=datetime.date(datetime.today())
print('date: ',d)
t=datetime.time(datetime.now())
print('time: ',t)
print('date components: ',d.day, d.month, d.year)
print('time components:',t.hour, t.minute, t.second)

#code to greet automatically

from datetime import *

t=datetime.time(datetime.now())
z=int(t.strftime('%H')) # 24 hour format

if (z >= 5 and z < 12):
	print('good morning')
elif (z >= 12 and z < 16):
	print('good afternoon')
elif (z >= 16 and z < 20):
	print('good evening')
else:
	print('good night')








