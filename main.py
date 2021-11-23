import tweepy
import datetime as dt
import schedule
import time


api_key = 'DIimRfChhMYfu0yfXghDU6Byp'
api_secret = 'rbJY9y6mZxE7Fd2Hq9ZYyShe4tfhjwqYp2Zw3ry8KfAAFdDhX1'
access_token = '1452292588573241345-UEWqMCAFr04FBcoCeRVo7RPQATEIuq'
access_token_secret = 'PRt9Z7p4ijNn2ohb8D8ehRuKMPrydgyUggKiLjH5oLDDj'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

date1 = dt.datetime(year=2022, month=2, day=26)
date2 = dt.datetime(year=2022, month=3, day=12)
date3 = dt.datetime(year=2022, month=3, day=19)
date4 = dt.datetime(year=2022, month=3, day=26)
date5 = dt.datetime.now()
day1 = date1 - date5
day2 = date2 - date5
day3 = date3 - date5
day4 = date4 - date5

def Tcaz1():
  if date5 == date2:
      return str('วันนี้มีสอบ O-net น่ะ สำหรับใครที่สมัคร')
  else:
      return str('O-net เหลือเวลาเตรียมตัวอีก') + str(day1.days) + str('วัน')
      
def Tcaz2():
  if date5 == date2:
    return str('วันนี้มีสอบ gat กับ pat1 น่ะ')
  else:
    return str('Gat/Pat เหลือเวลาเตรียมตัวอีก') + str(day2.days) + str('วัน')

def Tcaz3():
  if date5 == date3:
    return str('วันนี้สอบ 9 สามัญ สู้ๆเหล่าแพทย์ทุกคน!!!')
  else:
    return str('9 สามัญ เหลือเวลาเตรียมตัวอีก')  + str(day3.days) + str('วัน')

def Tcaz4():
  if date5 == date4:
    return str('วันนี้สอบ วิชาเฉพาะแพทย์ สู้ๆเหล่าแพทย์ทุกคน!!!')
  else:
    return str('วิชาเฉพาะแพทย์ เหลือเวลาเตรียมตัวอีก') + str(day4.days) + str('วัน')

A = 'อีก ' + str(day1.days) + ' สำหรับสอบ #ONET' + '\n' + 'อีก ' + str(day2.days) + ' สำหรับสอบ #Gat #Pat ' + '\n' + 'อีก ' + str(day3.days) + ' สำหรับสอบ #9สามัญ' + '\n' + 'อีก ' + str(day4.days) + ' สำหรับสอบ #กสพท' + '\n' + '\n' +'#Tcas65 #dek65'

def Job():
  api.update_status(A)

schedule.every().day.at("23:13").do(Job)


while True:
 schedule.run_pending()