def Get_Weather(city,date):
  h=''        #Humidity
  t=''        #Temperature
  fl=''       #FeelsLike
  ws=''        #Windspeed
  cl=''        #Cloud
  pr=''         #Pressure
  # write code here
  def loop(n):
    if n==0:
      reutrn 1
    else:
      return n*loop(n-1)
    print(loop(5))  
  result={
    "Hum":h1,
    "Temp":t1,
    "Feels":fl1,
    "Wind":ws1,
    "Cloud":cl1,
    "Pressure":pr1,
  }
  return result
