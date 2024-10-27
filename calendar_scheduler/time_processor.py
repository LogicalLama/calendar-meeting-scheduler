import datetime
from dateutil.parser import parse as date_parse

# Convert call time string to datetime
def process_call_time(call_time_str):
    call_time = date_parse(call_time_str, fuzzy=True)
    
    now = datetime.datetime.now()
    if call_time.date() < now.date():
        call_time = call_time.replace(year=now.year, month=now.month, day=now.day)
        if call_time < now:
            call_time += datetime.timedelta(days=1)
    
    return call_time
