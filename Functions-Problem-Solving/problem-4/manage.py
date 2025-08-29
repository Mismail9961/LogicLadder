def unique_elements(list1, list2):
    unique = []
    
    for item in list1:
        if item not in list2 and item not in unique:
            unique.append(item)
    
    for item in list2:
        if item not in list1 and item not in unique:
            unique.append(item)
    
    return unique


# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

print("Unique elements:", unique_elements(list1, list2))
