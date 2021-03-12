import datetime
from twilio.rest import Client
import time

def send_message(text):
    number_from='+16613697877'
    number_to='+79255431190'
    account_sied='ACb55b2a180ed0fb41c7197845078a0dab'
    account_token='4acbfe98e7e4baf1b02713435fc88abf'
    client=Client(account_sied,account_token)
    messages=client.messages.create(body=text,from_=number_from,to=number_to)
    return messages.sid
def proverka(today):
    if today == 1:
        timetable=open ('вторник.txt','r',encoding='utf-8')
        timetable=timetable.read()
        message=f'Привет Илья, вот твоё расписание на вторник: {timetable}'
        send_message(message)
    if today == 2:
        timetable=open ('среда.txt','r',encoding='utf-8')
        timetable=timetable.read()
        message=f'Привет Илья, вот твоё расписание на среду: {timetable}'
        send_message(message)
    if today == 3:
        timetable=open ('четверг.txt','r',encoding='utf-8')
        timetable=timetable.read()
        message=f'Привет Илья, вот твоё расписание на четверг: {timetable}'
        send_message(message)
    if today == 4:
        timetable=open ('пятница.txt','r',encoding='utf-8')
        timetable=timetable.read()
        message=f'Привет Илья, вот твоё расписание на пятницу: {timetable}'
        send_message(message)
    if today == 5:
        timetable=open ('суббота.txt','r',encoding='utf-8')
        timetable=timetable.read()
        message=f'Привет Илья, вот твоё расписание на субботу: {timetable}'
        send_message(message)
    if today == 6:
        timetable=open ('воскресенье.txt','r',encoding='utf-8')
        timetable=timetable.read()
        message=f'Привет Илья, вот твоё расписание на воскресенье: {timetable}'
        send_message(message) 
    if today == 0:
        timetable=open ('понедельник.txt','r',encoding='utf-8')
        timetable=timetable.read()
        message=f'Привет Илья, вот твоё расписание на понедельник: {timetable}'
        send_message(message)
def main():
    now=datetime.datetime.now()
    run = True
    day=now.replace(hour=6,minute=30)
    weekday=datetime.datetime.today().weekday()
    while run:
        if now==day:
            proverka(weekday)
            time.sleep(60)

if __name__ == '__main__':
    main()
