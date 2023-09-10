# ----------@sen ------------
# Exercise 10

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

merged_list=[]

for i in list1:
    if i %2 != 0:
        merged_list.append(i)
        
for i in list2:
    if i %2 == 0:
        merged_list.append(i)
        
print(merged_list)