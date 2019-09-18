def sort(list):
    if (len(list) > 1):
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]

        sort(left)
        sort(right)

        i = 0
        j = 0
        k = 0

        while (i < len(left) and j < len(right)):
            if (left[i] < right[j]):
                list[k] = left[i]
                i+=1
            else:
                list[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            list[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            list[k] = right[j]
            j+=1
            k+=1

def find_odd_even(list, even, odd):
    for num in list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

if __name__ == '__main__':
    size = input()
    list = [int(i) for i in input().split()]
    if (len(list) != int(size)):
        print("el tamaño del array y el número introducido no coinciden")
        quit()

    even = []
    odd = []
    find_odd_even(list, even, odd)
    sort(even)
    sort(odd)

    list = odd + even
    print(*list)
