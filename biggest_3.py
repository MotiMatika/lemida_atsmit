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


#הגבוה מבין 6 מספרים
#2 הפונקציות הראשונות מחזירות את המספר הגבוה מבין השלשה שהיא מקבלת
#השלישית מקבלת את 2 הגבוהים ומדפיסה את הגבוה
# def biggest1_3(a,b,c):
#     max_1 = max(a,b,c)
#     return(max_1)
# A=biggest1_3(1,20,3)

# def biggest4_6(a,b,c):
#     max_2 = max(a,b,c)
#     return(max_2)
# B=biggest4_6(59,6,78)

# def biggest1_6(A,B):
#     maxx = max(A,B)
#     return maxx
# C=biggest1_6(A,B)
# print(C)





import random
a=random.randint(1,100)
b=random.randint(1,100)
c=random.randint(1,100)
print("\nthe first  3 numbers : ",a,b,c)
def biggest1_3(a,b,c):
    max_1 = max(a,b,c)
    return(max_1)
A=biggest1_3(a,b,c)

d=random.randint(1,100)
e=random.randint(1,100)
f=random.randint(1,100)
print("the second 3 numbers : ",d,e,f)
def biggest4_6(d,e,f):
    max_2 = max(d,e,f)
    return(max_2)
B=biggest4_6(d,e,f)

def biggest1_6(A,B):
    maxx = max(A,B)
    return maxx
C=biggest1_6(A,B)
print("the biggest  of the 6 numbers is : ", C)