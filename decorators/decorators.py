# decorator is a normal functuion it contain a inner function .the no of paramatr of inner function is equal to the tha parameters of the actual fnction
def swap_num(fn):
    def inner_fn(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return inner_fn
@swap_num
def sub(n1,n2):
    return n1-n2
@swap_num
def div(n1,n2):
    return n1/n2

print (sub(2,8))
print(div(2,8))