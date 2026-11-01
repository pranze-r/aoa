#1-----k-small_large---


n = int(input("Enter the number of elements: "))

print("Enter the elements:")
arr = list(map(int, input().split()))

k = int(input("Enter the value of k: "))

arr.sort()

print("Sorted Array:", arr)

print("1. K-th Smallest")
print("2. K-th Largest")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    print(k, "th Smallest Element:", arr[k - 1])

elif choice == 2:
    print(k, "th Largest Element:", arr[n - k])

else:
    print("Invalid Choice")


#2------Radix Sort-----


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_value = max(arr)

    exp = 1

    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr


arr = [170, 45, 75, 90, 802, 24]

print("Original:", arr)
radix_sort(arr)
print("Sorted:", arr)


#3-----Bubble sort----


def bubble_sort(a):
    n=len(a)

    for i in range(n):
        swapped=False

        for j in range(0,n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swapped=True
        if not swapped:
            break
        return a

test_a = [10,45,68,11,26,34,41]
print("unseorted array: ", test_a)
print("sorrted array: ", bubble_sort(test_a))


    

    


#4----Bucket Sort------


def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    max_value = max(arr)

    bucket_count = 5

    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = (num * bucket_count) // (max_value + 1)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_array = []

    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


arr = [42, 32, 33, 52, 37, 47, 51]

print("Original Array:", arr)

sorted_arr = bucket_sort(arr)

print("Sorted Array:", sorted_arr)




#-----counting sort---

def counting_sort(arr):
    max_value = max(arr)

    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1

    index = 0

    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1

    return arr


arr = [4, 2, 2, 8, 3, 3, 1]

print("Original Array:", arr)
counting_sort(arr)
print("Sorted Array:", arr)



#5----MedianofMedian------


n1 = int(input("Enter the number of elements in Array 1: "))

print("Enter the elements of Array 1:")
arr1 = list(map(int, input().split()))

n2 = int(input("Enter the number of elements in Array 2: "))

print("Enter the elements of Array 2:")
arr2 = list(map(int, input().split()))

arr = arr1 + arr2

arr.sort()

print("Merged Sorted Array:", arr)

n = len(arr)

if n % 2 == 1:
    median = arr[n // 2]

else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2

print("Median:", median)



