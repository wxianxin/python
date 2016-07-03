def answer(str):
    # your code here
    num = []
    sign = []
    
    result = []
    sentinel_p = False
    sentinel_p1 = False
    sentinel_m = False
    
    l = len(str)
    for i in reversed(range(0,l,2)):
        num.append(str[i])
        if i>0:
            sign.append(str[i-1])
    
    for i in range(len(sign)):
        if sign.pop() == "+" and sentinel_p == False:
            sentinel_p = True
            sentinel_m = False
            sentinel_p1 = True
            continue
        if sign.pop() == "+" and sentinel_p == True:
            result.append(num.pop())
            result.append(num.pop())
            result.append("+")
            continue
        if sign.pop() == "*" and sentinel_p == True:
            result.append(num.pop())
            sentinel_p = False
            continue
        if sign.pop() == "*" and sentinel_m == False:
            sentinel_p = False
            sentinel_m = True
            result.append(num.pop())
            result.append(num.pop())
            result.append("*")
            continue
        if sign.pop() == "*" and sentinel_m == True:
            result.append(num.pop())
            result.append("*")
            continue
            
    return result   
