# Write a program for basic array operations (insert, delete and search an element).


arr = list(map(int, input('enter array elements: ').split()))
print(f'Inserted array is:\n{arr}')
while True:
    print('\n1. Insert')
    print('2. Delete')
    print('3. Search')
    print('4. Display')
    print('5. Exit')
    choice = int(input('enter your choice: '))
    if choice == 1:
        element = int(input('enter element to insert: '))
        position = int(input('enter position: '))
        arr.append(0)
        for i in range(len(arr) - 1, position, -1):
            arr[i] = arr[i-1]
        arr[position] = element
        print(arr)
        print('element inserted successfully.')
    elif choice == 2:
        element = int(input('enter element to delete: '))
        if element in arr:
            index = arr.index(element)
            for i in range(index, len(arr) - 1):
                arr[i] = arr[i+1]
            arr.pop()
            print(arr)
            print(f'element deleted successfully.\nupdated array is: {arr}')
        else:
            print('element not found')
    elif choice == 3:
        element = int(input('enter element to search: '))
        found = False
        for i in range(len(arr)):
            if arr[i] == element:
                print(f'element found at index {i}')
                found = True
                break
        if not found:
            print('element not found')
    elif choice == 4:
        print(f'Array: {arr}')
    elif choice == 5:
        break
    else:
        print('invalid choice')
        