def Get_Weather(city,date):
  class dayWeather:
    def __init__(self,date,h,t,fl,ws,cl,pr):
      #attributes
      self.date=date
      self.h=h      #Humidity
      self.t=t      #Temperature
      self.fl=fl    #FeelsLike
      self.ws=ws    #Windspeed
      self.cl=cl    #Cloud
      self.pr=pr    #Pressure
  # write code here

  # Getting date Range
  import datetime
  from datetime import date as dt                            #Import date from datetime library
  def loop(n):
      if n<=1:
          if n<=0:                                        
              print('The weather on '+date2+' is:')      #In case the date is before current day
          return 1                                     
      else:
          base=dt.today()                              #alloting base date
          print(base+datetime.timedelta(days=n))       #printing the days
          return n*loop(n-1)                              
  date1=str(dt.today())                                #Taking Today's Date as Date1
  date2=input('Enter the second date: ')                 #Taking date entered as Date2
  datetime1=dt.fromisoformat(date1)                    #Taking date1 in numerical form
  datetime2=dt.fromisoformat(date2)                    #Taking date2 in numerical form
  x=str(datetime2-datetime1)                             #Substracting two dates
  l=x.split()                                            #spliting x into ['No of days','days','00:00:00']                                 
  print(loop(int(l[0])))                                 #considering No of days in the list and calling the function from the loop function

  def weightedAvg(d1,d2,d3,d4,d5):
    d=((d11*9)+(d2*6)+(d3*5)+(d4*4)+(d5*2))/26
    return d

  def paramCalc(n, d1, d2, d3, d4, d5):
    if n == 1:
        return d1
    elif n == 2:
        return d2
    elif n == 3:
        return d3
    elif n == 4:
        return d4
    elif n == 5:
        return d5
    else:
        # Recursively calculate the parameter for day n as the average of the past 5 days
        param_n_minus_1 = paramCalc(n - 1, d1, d2, d3, d4, d5)
        param_n_minus_2 = paramCalc(n - 2, d1, d2, d3, d4, d5)
        param_n_minus_3 = paramCalc(n - 3, d1, d2, d3, d4, d5)
        param_n_minus_4 = paramCalc(n - 4, d1, d2, d3, d4, d5)
        param_n_minus_5 = paramCalc(n - 5, d1, d2, d3, d4, d5)
        return weightedAvg(param_n_minus_1, param_n_minus_2, param_n_minus_3, param_n_minus_4 ,param_n_minus_5)

  result={
    "Hum":h1,
    "Temp":t1,
    "Feels":fl1,
    "Wind":ws1,
    "Cloud":cl1,
    "Pressure":pr1,
  }
  return result
