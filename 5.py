def test(x,y):
    if x==y or abs(x-y)==5 or (x+y)==5:
        return true
    else:
        return false
x=int(input("enter the number : "))
y=int(input("enter the number : "))    
test(x,y)

