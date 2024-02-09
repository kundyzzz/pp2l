def spy(nums):
    index_0 = None
    index_1 = None
    index_2 = None
    
    for i, num in enumerate(nums):
        if num == 0 and index_0 is None:
            index_0 = i
        elif num == 0 and index_0 is not None and index_1 is None:
            index_1 = i
        elif num == 7 and index_0 is not None and index_1 is not None:
            index_2 = i
            break
    
    if index_0 is not None and index_1 is not None and index_2 is not None:
        return True
    else:
        return False

print(spy([1,2,4,0,0,7,5]))
print(spy([1,7,2,0,4,5,0]))