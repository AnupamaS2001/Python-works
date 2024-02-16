def capitalize(fn):
    def wrapper():
       res=fn()
       res=res.upper()
       return res
    return wrapper

@capitalize
def morning_greetings():
    return "good morning"

@capitalize
def evening_greetings():
    return "good evening"

print(morning_greetings())
print(evening_greetings())