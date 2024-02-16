def perform_operatons(*args,**kwargs):
    num1,num2=args
    op=kwargs.get("operand")
    if op=="+":
        return num1+num2
    elif op=="-":
        return num1-num2
    elif op=="*":
        return num1*num2
    else:
        return "invalid operand"
    
print(perform_operatons(10,20,operand="+"))