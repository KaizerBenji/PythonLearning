# Simple Sorting Algorithm using built in Python support

array = [9, 4, 2, 5, 7, 2, 6]
array.sort()
print(array)

sorted_array = sorted(array)
print(array)

array.sort(reverse=True)
print(array)

# Bubble Sorting, slow and inefficient


def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i + 1]:
                # swap elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # set the flag True so it will loop
                swapped = True


array2 = [11, 5, 72, 3, 9, 21, 6]
bubble_sort(array2)
print(array2)
