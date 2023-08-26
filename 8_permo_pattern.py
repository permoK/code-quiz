#this function prints out a pattern 
def pattern():
    for i in range(1,6):
        for j in range(i):
            print(i, end='')
        print("\n")
pattern()