def sumNum(x,y):
    return x+y
    
def ssum(x,y):
    print(type(x),type(y))
    if type(x)==type(y):
        num=sumNum(x,y)
        return num
    else:
        a="you should sync type"
        return a
    

if __name__=="__main__":
    print(ssum('k',5))
    print(ssum(1,5))
    print(ssum(50,3.14))