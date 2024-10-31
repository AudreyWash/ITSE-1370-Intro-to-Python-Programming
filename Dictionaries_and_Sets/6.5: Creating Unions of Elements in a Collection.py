def unite_lists(list1, list2):
    result = []
    
    for element in list1:
        if element not in result:
            result.append(element)
    
    for element in list2:
        if element not in result:
            result.append(element)
    
    return result

if __name__ == '__main__':
    print(unite_lists([2, 4, 6, 8], [3, 6, 9, 12]))