import datetime 
    
# using now() to get current time 
current_time = datetime.datetime.now() 

print (current_time.year) 

print (current_time.month) 

datetimeStr = current_time.strftime("%Y %b")
print (datetimeStr) 
fileUrl="https://archives.nseindia.com/content/historical/EQUITIES/2021/AUG/cm13AUG2021bhav.csv.zip"
YEAR=current_time.strftime("%Y")
MONTH=current_time.strftime("%b")
DAY=current_time.strftime("%d")
fileUrl="https://archives.nseindia.com/content/historical/EQUITIES/" + YEAR +"/"+MONTH+"/cm"+DAY+MONTH+YEAR+"bhav.csv.zip"
print(fileUrl)

print('-'*80)



intMonth=1
intDay=1
months = [datetime.date(2000, m, 1).strftime('%b') for m in range(1, 13)]
for month in months:
  print (month.upper())
  
def month_year_iter( start_month, start_year, end_month, end_year ):
    ym_start= 12*start_year + start_month - 1
    ym_end= 12*end_year + end_month - 1
    for ym in range( ym_start, ym_end ):
        y, m = divmod( ym, 12 )
        yield y, m+1

#for m in month_year_iter(1, 2010, 2, 2011):
    #print (m)
print('-'*80)

import calendar
 
c = calendar.Calendar()
for date in c.itermonthdates(2016, 6):
  print(date)
print('-'*80)