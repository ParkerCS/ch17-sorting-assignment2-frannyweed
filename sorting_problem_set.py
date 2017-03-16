# Problem 1 - Value Swap (2pts)
# Swap the values 18 and 38 in the list below
my_list = [27, 32, 18,  2, 11, 57, 14, 38, 19, 91]
hold = my_list[2]
my_list[2] = my_list[7]
my_list[7] = hold
print(my_list)

# Problem 2 - Selection Sort (8 pts)
# Make a selection sort FUNCTION which takes in 1 parameter (the list),
# sorts it and RETURNS the sorted list.  Then sort and print the result
# of the following list.
sort_me = [655, 722, 736, 314, 59, 778, 632, 477, 230, 556, 353, 769, 622, 731, 683, 233, 524, 186, 694, 507, 443, 833, 270, 373, 567, 775, 34]
def selection(list):
    for pos in range(len(list)):
        min_pos = pos
        for scan_pos in range(min_pos, len(list)):
            if list[scan_pos] < list[min_pos]:
                min_pos = scan_pos
        temp = list[pos]
        list[pos] = list[min_pos]
        list[min_pos] = temp
    return list
print(selection(sort_me))

# Problem 3 - Insertion Sort (8 pts)
# Make an insertion sort FUNCTION which takes in 1 parameter (the list),
# sorts it and RETURNS the sorted list.  Then sort and print the result
# of the following list.
sort_me2 = [551, 138, 802, 954, 569, 372, 454, 366, 936, 959, 958, 202, 474, 658, 108, 424, 523, 611, 557, 0, 733, 903, 788, 850, 11, 12, 975]
def insertion(list):
    for pos in range(1, len(list)):
        key_pos = pos
        scan_pos = key_pos - 1
        key_val = list[key_pos]
        while scan_pos >= 0 and list[scan_pos] > key_val:
            list[scan_pos + 1] = list[scan_pos]
            scan_pos -= 1
        list[scan_pos + 1] = key_val
    return list
print(insertion(sort_me2))

# Problem 4 - Efficiency? (10 pts)
# Modify your two functions so that they track the number of times
# you iterate through the big loop, and the inner loop of the sort.
# Make the functions print each value.  Run the sorts on the list below.

sort_me3 = [77, 29, 59, 69, 86, 40, 47, 40, 74, 44, 58, 78, 9, 8, 13, 99, 3, 57, 19, 48, 55, 50, 94, 69, 98, 30, 37, 29, 40, 29, 36, 32, 26, 85, 61, 51, 70, 96, 90, 89, 91, 88, 68, 4, 4, 74, 15, 72, 5, 91, 76, 6, 56, 80, 72, 87, 63, 86, 48, 24, 17, 23, 30, 41, 7, 64, 16, 19, 40, 63, 14, 95, 44, 58, 1, 6, 45, 55, 52, 54, 44, 36, 50, 6, 96, 66, 8, 46, 48, 48, 75, 25, 39, 30, 70, 44, 38, 90, 49, 70]

def selection2(list):
    big_selection = 0
    small_selection = 0
    for pos in range(len(list)):
        min_pos = pos
        for scan_pos in range(min_pos, len(list)):
            if list[scan_pos] < list[min_pos]:
                min_pos = scan_pos
            small_selection += 1
        temp = list[pos]
        list[pos] = list[min_pos]
        list[min_pos] = temp
        big_selection += 1
    print(big_selection)
    print(small_selection)
    return list
print(selection2(sort_me))

sort_me2 = [551, 138, 802, 954, 569, 372, 454, 366, 936, 959, 958, 202, 474, 658, 108, 424, 523, 611, 557, 0, 733, 903, 788, 850, 11, 12, 975]
def insertion2(list):
    big_insertion = 0
    small_insertion = 0
    for pos in range(1, len(list)):
        key_pos = pos
        scan_pos = key_pos - 1
        key_val = list[key_pos]
        while scan_pos >= 0 and list[scan_pos] > key_val:
            list[scan_pos + 1] = list[scan_pos]
            scan_pos -= 1
            small_insertion += 1
        big_insertion += 1
        list[scan_pos + 1] = key_val
    print(big_insertion)
    print(small_insertion)
    return list
print(insertion2(sort_me2))
