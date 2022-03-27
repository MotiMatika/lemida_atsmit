def biggest (a,b,c):
    if a==b==c:
        print("\nall numbers are equal")
        quit()

    if a>b and a>c:
        return a
    elif a>b and c>a:
        return c
        
    if b>c and b>c:
        return b    
    elif b>a and b<c:
        return c 
    
       
        
print(biggest(1,12,33))