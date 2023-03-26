a = [1, 2]
b = [1, 2, 3]
c = [1, 2, 3, 4, 5]

arr=[a, b, c]

maxLineLen = max(map(len, arr))

for i in range(maxLineLen): 
    for p in range(3):
        print("printer: ", p)
        l = arr[p]
        if i >= len(l): 
            print("NO STRING")
        else: 
            print(l[i])