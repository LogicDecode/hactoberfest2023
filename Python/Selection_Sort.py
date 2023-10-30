# Selection Sort algorithm

def SelectionSort(arr):
    """ Sort given array using Selection Sort algorithm and return sorted array """
    for i in range(len(arr)):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        (arr[i], arr[mini]) = (arr[mini], arr[i])
    return arr

if __name__ == "__main__":
    print('Enter numbers space separated : ', end=' ')
    numbers = [int(x) for x in input().split()]
    numbers = SelectionSort(numbers)
    for i in numbers:
        print(i, end=' ')