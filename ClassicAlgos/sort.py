def bubbleSort(foo: list):
    
    if len(foo) <= 0: return
    
    isAscending = False
    
    while not isAscending:
        for i in range(1, len(foo)):
            if foo[i] < foo[i-1]:
                isAscending = False 
                foo[i], foo[i-1] = foo[i-1], foo[i]
            else:
                isAscending = True

nums = [2,3,4,1,8,5,3,9,23,4]

bubbleSort(nums)

print(nums)