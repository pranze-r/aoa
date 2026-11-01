#1--Bubble sort--

arr = list(map(int, input("Enter numbers: ").split()))

n = len(arr)

for i in range(n):
    swapped = False

    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True

    if not swapped:
        break

print("Sorted array:", arr)

#2---Selection Sort--


arr = list(map(int, input("Enter numbers: ").split()))

n = len(arr)

for i in range(n):
    min_index = i

    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array:", arr)


#3---Insertion Sort---

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


arr = list(map(int, input("Enter numbers: ").split()))

print("Sorted array:", insertion_sort(arr))


#4 ---Merge Sort--

def merge_sort(a):
    if len(a)<=1:
        return a
    midd = len(a)//2
    
    left_side=a[:midd]
    right_side=a[midd:]

    left_sorted= merge_sort(left_side)
    right_sorted= merge_sort(right_side)

    def merge(left,right):
        sorted_array=[]
        i=j=0

        while i<len(left) and j <len(right):
            if left[i]<right[j]:
                sorted_array.append(left[i])
                i+=1
            else:
                sorted_array.append(right[j])
                j+=1

        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])

        return sorted_array
    return merge(left_sorted, right_sorted)

test_a=[10,45,68,11,26,34,41]
print("unsorted array: ",test_a)
print("sorted array: ",merge_sort(test_a))



#5-- quick sort


def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[-1]

    left = [x for x in a[:-1] if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a[:-1] if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr = list(map(int, input("Enter numbers: ").split()))

print("Sorted array:", quick_sort(arr))
