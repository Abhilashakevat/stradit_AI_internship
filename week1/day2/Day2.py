#DAY 2
#T1
name=input('Enter name:')
age=int(input('Enter age:'))
height=float(input('Enter height:'))
c_pref=input('Enter coffee preference:')
print(f'{"NAME:",name,"AGE:",age,"HEIGHT:",height,"Prefarable 
coffee:",c_pref}')
print(f" my age:{age+1}")
print(f"|{name}|")
print(f"Height:{height:.1f}")
print(f"Height:{height:.2f}")
Enter name: abhilasha 
Enter age: 12
Enter height: 3.5
Enter coffee preference: cold
('NAME:', 'abhilasha ', 'AGE:', 12, 'HEIGHT:', 3.5, 'Prefarable 
coffee:', 'cold')
 my age:13
|abhilasha |
Height:3.5
Height:3.50
#T2
no1=int(input('Enter no 1:'))
no2=int(input("Enter no 2:"))
print("ADDITION OF TWO NO:",no1+no2)
print("DIFFERENCE:",no1-no2)
print("PRODUCT:",no1*no2)
print("DIVISON float no:",no1/no2)
print("Division return integer:",no1//no2)
print("Exponetiation:",no1**no2)
print("reminder:",no1%no2)
Enter no 1: 10
Enter no 2: 5
ADDITION OF TWO NO: 15
DIFFERENCE: 5
PRODUCT: 50
DIVISON float no: 2.0
Division return integer: 2
Exponetiation: 100000
reminder: 0
#T3
birth_y=int(input('enter your birth year:'))
age=2026-birth_y
print("age is:",age)
enter your birth year: 2004
age is: 22
#T4
tempr=float(input('enter temprature:'))
F=(tempr*9/5)+32
print("temprature in Fahrenheit:",F)
print(f" Temprature {F:.1f}")
enter temprature: 33.56
temprature in Fahrenheit: 92.408
 Temprature 92.4
#T5
str1=input("Enter No:")
print("length of string:",len(str1))
print("first char of string:",str1[0])
print("in upper case:",str1.upper())
print("in lower case:",str1.lower())
print("print last char:",str1[-1])
print("reverse the string:",str1[::-1])
Enter No: abhi
length of string: 4
first char of string: a
in upper case: ABHI
in lower case: abhi
print last char: i
reverse the string: ihba
#T6
price=int(input("Enter price:"))
qnt=int(input("enter quantity:"))
total_p=price*qnt
tax=total_p*18//100
o_price=total_p-tax
print("Original price one product:",price)
print("quantity:",qnt)
print("total price:",total_p)
print("after reduction of tax:",o_price)
Enter price: 120
enter quantity: 5
Original price one product: 120
quantity: 5
total price: 600
after reduction of tax: 492
#T7
n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
n3=int(input("enter n3:"))
print("average:",(n1+n2+n3)//3)
print("mininun no:",min(n1,n2,n3))
print("maximum no:",max(n1,n2,n3))
enter n1: 11
enter n2: 12
enter n3: 13
average: 12
mininun no: 11
maximum no: 13
