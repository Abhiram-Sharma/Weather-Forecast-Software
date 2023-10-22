def Get_Weather(city,date):
  h=''        #Humidity
  t=''        #Temperature
  fl=''       #FeelsLike
  ws=''        #Windspeed
  cl=''        #Cloud
  pr=''         #Pressure
  # write code here
from datetime import date
def loop(n):
    if n<=0:
        print('The weather on that date was :')
        return 1
    else:
        
        return n*loop(n-1)
date1=str(date.today())
date2=input('Enter the second date: ')
datetime1=date.fromisoformat(date1)
datetime2=date.fromisoformat(date2)
x=str(datetime2-datetime1)
l=x.split()   
print(loop(int(l[0]))) 
  result={
    "Hum":h1,
    "Temp":t1,
    "Feels":fl1,
    "Wind":ws1,
    "Cloud":cl1,
    "Pressure":pr1,
  }
  return result
