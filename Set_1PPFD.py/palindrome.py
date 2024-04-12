

def palindrome():
    while True:
        try:
            n = int(input("Enter the number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    temp = n
    rev = 0
    
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    
    if rev == temp:
        print("Palindrome") 
    else:
        print("Not a Palindrome") 

palindrome()
