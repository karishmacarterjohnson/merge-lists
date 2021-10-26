def mergeSortTwoLists(list1, list2):
    sorted = []
    i = j = 0
    while i < len(list1) and j < len(list2): 
        if list1[i] < list2[j]:
            sorted.append(list1[i])
            i += 1
        else:
            sorted.append(list2[j])
            j += 1
        #k += 1
    while i < len(list1):
        sorted.append(list1[i])
        i += 1
    while j < len(list2):
        sorted.append(list2[j])
        j += 1
    return sorted