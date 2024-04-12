
n = int(input("Enter total number of elements: ")) 

L1 = []
for i in range(n): 
    k = int(input()) 
    L1.append(k) 
L1 = sorted(L1)
print(f"Ascending order: {L1}") 
print(f"Descending order: {L1[::-1]}")
