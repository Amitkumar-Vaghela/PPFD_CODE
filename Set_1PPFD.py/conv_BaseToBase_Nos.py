
n = input("Enter the value to convert: ")
Fb = int(input("Enter the base value from which you want to convert: "))
tb = int(input("Enter the base value to which you want to convert (2, 8, 10, or 16): "))

Dv = int(str(n), Fb)

if tb == 16:
    Cv = format(Dv, 'X') 
else:
    Cv = format(Dv, 'b' if tb == 2 else '' if tb == 10 else 'o') 

print(Cv)
