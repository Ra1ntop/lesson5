import math
print('reshim ax^2+bx+c=0')
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=b*b-4*a*c
if d > 0:
    x1=(-b+math.sqrt(d))/2*a
    x2=(-b-math.sqrt(d))/2*a
    print(f"pervii korx1}, \nvtor kor {x2}")
elif d==0:
    x=-b/2*a
    print(f"kor {x}")
else:
    print('kor net')
    
    
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

if ((a+b)<c) or ((a+c)<b) or ((b+c)<a):
    print("Treyg net")
else:
    if a==b and b==c:
        print("ravnostor")
    elif a==b or b==c :
        print("Равнобе.")
    else:
        print("Разно.")





print("введите координаты точки A(x;y)")
x = int(input("x="))
y = int(input("y="))
if x>0 and y>0:
    print("в 1 четверти")
elif x<0 and y>0:
    print("в 2 четверти")
elif x<0 and y<0:
    print("в 3 четверти")
else:
    print("в 4 четверти")
    
    
    


x = int(input("введите x: "))
if x>0:
    y = 2x-10
    print(y)
elif x<0:
    y = 2abs(x)- 1
    print(y)
else:
    y=0
    print(y)
