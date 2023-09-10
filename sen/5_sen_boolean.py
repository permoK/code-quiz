# ------------- @sen ----------------------
# excercise 4

l_1=[1,2,3,1]
l_2=[1,2,3,4]

def numcheker(lists):
    print(f'Given {lists}')
    fnum=lists[0]
    lnum=lists[-1]
    
    if fnum == lnum:
        return True
    else:
        return False
    
print('Results is ', numcheker(l_1))
print('Results is ', numcheker(l_2))