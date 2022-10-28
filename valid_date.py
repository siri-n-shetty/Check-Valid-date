date = input("Enter the date in format dd/mm/yyyy  ")
dd,mm,year = date.split("/")
dd = int(dd)
mm = int(mm)
year = int(year)
if (mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max = 31
elif (mm==4 or mm==6 or mm==9 or mm==11):
    max = 30
elif (year%4==0 or year%100==0 or year%400==0):
    max = 29
    print("Leap year")
else:
    max = 28
if (mm<1 or mm>12):
    print("Date is invalid")
elif (dd<1 or dd>max):
    print("Date is invalid")
elif (dd==31 and mm==12):
    dd=1
    mm=1
    year=year+1
    print("Date is valid and the next date is = ", dd,"/",mm,"/",year)
elif (dd==max and mm<12):
    dd=1
    mm=mm+1
    print("Date is valid and the next date is = ", dd,"/",mm,"/",year)
else:
    dd=dd+1
    print("Date s valid and the next date is = ", dd,"/",mm,"/",year)