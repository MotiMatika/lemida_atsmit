# פונקציה שמקבלת שלשה מספרים ומחזירה את הגדול מביניהם
#גירסה ארוכה
# def biggest (a,b,c):
#     if a==b==c:
#         print("\nall numbers are equal")
#         quit()

#     if a>b and a>c:
#         return a
#     elif a>b and c>a:
#         return c
        
#     if b>c and b>c:
#         return b    
#     elif b>a and b<c:
#         return c 
            
# print(biggest(1,12,33))


#גירסה קצרה
# def biggest (a,b,c):
#     max_number = max(a,b,c)
#     return max_number

# print(biggest(1,12,33))


def biggest1(a,b,c):
    max_1 = max(a,b,c)
    return(max_1)
biggest1(1,2,3)


