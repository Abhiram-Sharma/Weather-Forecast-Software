def Get_Weather(city,date):
  h=''        #Humidity
  t=''        #Temperature
  fl=''       #FeelsLike
  ws=''        #Windspeed
  cl=''        #Cloud
  pr=''         #Pressure
  # write code here
import datetime
from datetime import date                              #Import date from datetime library
def loop(n):
    if n<=1:
        if n<=0:                                        
            print('The weather on '+date2+' is:')      #In case the date is before current day
        return 1                                     
    else:
        base=date.today()                              #alloting base date
        print(base+datetime.timedelta(days=n))       #printing the days
        return n*loop(n-1)                              
date1=str(date.today())                                #Taking Today's Date as Date1
date2=input('Enter the second date: ')                 #Taking date entered as Date2
datetime1=date.fromisoformat(date1)                    #Taking date1 in numerical form
datetime2=date.fromisoformat(date2)                    #Taking date2 in numerical form
x=str(datetime2-datetime1)                             #Substracting two dates
l=x.split()                                            #spliting x into ['No of days','days','00:00:00']                                 
print(loop(int(l[0])))                                 #considering No of days in the list and calling the function from the loop function
  result={
    "Hum":h1,
    "Temp":t1,
    "Feels":fl1,
    "Wind":ws1,
    "Cloud":cl1,
    "Pressure":pr1,
  }
  return result
