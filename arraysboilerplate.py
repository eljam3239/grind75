def insertEnd(arr,n,length, capaacity):
    if length<capacity):
        arr[length]=n

def removeEnd(arr,length):
    if length > 0:
        arr[length-1] = 0

def insertMiddle(arr, i, n, length):
    for index in range(length-1, i-1, -1):
        arr[index+1] = arr[index]

    arr[i] = n
def removeMiddle(arr, i, length):
    for index in range(1+1, length):
        arr[index-1] = arr[index]


