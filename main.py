
#Q1
m=int(input("Enter marks"))
if(m>80):
    print(" Grade A")
elif(60<=m<=80):
    print(" Grade B")
elif(50<=m<60):
    print(" Grade C")
elif(45<=m<50):
    print(" Grade D")
elif(25<=m<45):
    print(" Grade E")
elif(m<25):  
    print(" Grade F")
else:
    print(" invalid grade")
#Q2  
n= int(input("Enter year: "))
if(n%400==0 and n%100==0):
    print("Leap year")
elif(n%4 ==0 and n%100!= 0):
        print("Leap year")
else:
        print('not a leap year')
       
#Q3
a= int(input("4*3="))
if (a==12):
    print ("right")
else:
    print("wrong")
   
b= int (input("5*8="))
if (b==40):
    print ("right")
else:
    print("wrong")
   
c= int(input("9*9="))
if(c==81):
    print("right")
else:
    print("wrong")
d= int(input("20*10="))
if(d==200):
    print("right")
else:
    print("wrong")
   
e= int(input("9*3="))
if(e==27):
    print("right")
else:
    print =("wrong")
f= int(input("4*9="))
if(f==36):
    print("right")
else:
    print("wrong")
g= int(input("9*7="))
if(g==63):
        print("right")
else:
    print =("wrong")
   
h=int(input("7*8="))
if(h==56):
        print("right")
else:
    print =("wrong")

i= int(input("8*3="))
if(i==24):
        print("right")
else:
    print =("wrong")
   
j= int(input("10*3="))
if(j==30):
        print("right")
else:
    print =("wrong")

print("thanks for playing")

#Q4
for i in range(200):
           
    if i % 5 == 2:
         if i % 6 ==3:
            if i % 7 ==2:
              print(i, 'candies are in the bowl!')    

