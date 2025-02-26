from datetime import datetime

def now_time():
    now = datetime.now()
    day_of_week = now.strftime('%A')
    day_of_month = now.strftime('%d')   
    day_in_calendar = now.strftime('%d %B %Y')
    current_time = now.strftime('%H:%M:%S')
    
    status_date_now_message = f'{day_of_week}, {day_in_calendar} - LOGIN: {current_time}'
    return status_date_now_message


