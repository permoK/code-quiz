def odd_even(list1, list2):
    #declare an empty list 
    odd = []
    even = []
    #find the length of the list
    length = len(list1)
    for i in range(length):
        if list1[i] % 2 != 0:
            odd.append(list1[i])
        if list2[i]%2 == 0:
            even.append(list2[i])
    print(odd + even)
odd_even(list1=[10, 20, 25, 30, 35] ,list2=[40, 45, 60, 75, 90])