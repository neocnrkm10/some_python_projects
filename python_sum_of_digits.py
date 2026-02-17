
def sum(num):
    if num<10:
        return num
        
    else:
        str_num=str(num)
        new_num=0
        for i in range(len(str_num)):
            new_num+=int(str_num[i])
            
            
     
    return sum(new_num)
    
print(sum(2876))
        