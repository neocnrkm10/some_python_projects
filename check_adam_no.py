def reverse(n):
    ch = []
    st = str(n)

    for i in range(len(st)):
        ch.append(st[i])

    new = ""
    for i in range(len(st)):
        new = new + ch[-1]   
        ch.pop()

    return int(new)


def is_adam(n):
    
    if reverse(n)*reverse(n)==reverse(n*n):
        return True
        
    else:
        return False   
        
print(is_adam(12))        
        
        
        