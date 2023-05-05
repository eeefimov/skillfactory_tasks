#search
def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


#sort
def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


input_num = input("Enter numbers using space: ")
try:
    numbers = list(map(int, input_num.split()))
except ValueError:
    print("Error input")
else:
    search_number = input("Enter number: ")
    try:
        search_number = int(search_number)
    except ValueError:
        print("Error: ValueError")
    else:
        sorted_list = sort_list(numbers)
        print(sorted_list)


SRT = binary_search(sorted_list, search_number, 0, len(sorted_list) - 1)
print(SRT)
if not SRT:
    print("Number is not in the list")
    exit()
else:
    for i in range(SRT, len(sorted_list)):
        if sorted_list[i] >= search_number:
            print(f"Position of the element is: {i-1}")
            break