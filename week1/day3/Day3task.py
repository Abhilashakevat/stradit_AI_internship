#Day3
#T1
age=int(input("Enter your age:\n"))
if age<=12 and age>0:
    print("category:child")
elif age>=13 and age<=17:
    print("category:Teenager")
elif age>=18 and age<=24:
    print("category:Young Adults")
elif age>=25 and age<=59:
    print("category:Adults")

elif age>=59 and age<=150:
    print("category:Senior")
else:
    print("invalid age")