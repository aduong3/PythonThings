import random
def binSearch(arr,low,high,keyFind):
    if(low > high):
        return -1
    mid = (high + low)//2
    if arr[mid] == keyFind:
        return mid
    if keyFind < arr[mid]:
        return binSearch(arr,low,mid-1,keyFind)
    elif keyFind > arr[mid]:
        return binSearch(arr,mid+1,high,keyFind)

def insertSort(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        while(i >= 0 and arr[i] > key):
            arr[i+1] = arr[i]
            i -=1
        arr[i+1] = key
    return arr

def main():
    arr = []
    size = int(input("Please insert a number for the array size: "))
    max = int(input("What is the max value you want (0-#): "))
    keyFind = int(input("What value do you want to find? "))
    for i in range(size):
        rand = random.randint(0,max)
        arr.append(rand)
    print(f"This is the random array:\n{arr}")
    insertSort(arr)
    print(f"This is the sorted array:\n{arr}")
    
    result = binSearch(arr, 0,size-1,keyFind)
    if(result != -1):
        print(f"We have found your value at index {result}")
    else:
        print("It is not in the array.")

if __name__ == '__main__':
    main()