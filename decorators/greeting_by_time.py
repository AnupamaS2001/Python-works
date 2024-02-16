def capitalize(fn):
    def wrapper():
       res=fn()
       res=res.upper()
       return res
    return wrapper

from datetime import datetime
current_time=datetime.now()
current_hour=current_time.hour

print(current_hour)
@capitalize
def greeting_by_time():

    current_time=datetime.now()
    current_hour=current_time.hour
    if(5<=current_hour<12):
        return "good morning"
    elif(12<=current_hour<18):
        return "good afternoon"
    else:
        return  "good evening"
print(greeting_by_time())