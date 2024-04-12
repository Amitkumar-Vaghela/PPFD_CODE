year=int(input("Enter year\n"))
if year%400==0 and year%100==0: 
 print("This year is leap year")
elif year%4==0 and year%100!=0: 
 print("This year is leap year") 
else :
 print("This year is not leap year")