from random import randint
import math

def partition(array, left, right):
    # median index
    pivot = array[math.floor((left + right)/2)]

    left = left
    right = right

    while left < right:
        while array[left] < pivot: # move on
            left += 1

        while array[right] > pivot: # move on
            right -= 1

        if left <= right: # swap elements
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    return left


def quicksort(array, left, right):
    if len(array) > 1:
        pivot_index = partition(array, left, right)

        if left < pivot_index - 1:
            quicksort(array, left, pivot_index - 1)

        if right > pivot_index:
            quicksort(array, pivot_index, right)


if __name__ == "__main__":
    size = 10
    array = [randint(0,100) for _ in range(size)]

    print ("Input array: ", array)

    quicksort(array, 0, len(array) - 1)

    print ("Sorted array: ", array)
