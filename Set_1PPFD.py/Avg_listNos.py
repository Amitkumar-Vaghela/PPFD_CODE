n = int(input("Enter the number of elements: ")) 
L1 = []
total_sum = 0

for i in range(n): 
    k = int(input(f"Enter element {i+1}: ")) 
    L1.append(k) 
    total_sum += k 

average = total_sum / n
print("Average:", average)
