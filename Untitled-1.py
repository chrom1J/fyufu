
new_list = [8, 3, 14, 5, 7, 10, 1, 2]

def small(list = []):
    m = len(list)
    for i in range(m-1):
        min = i
        for n in range(i+1, m):
            if list[n] < list[min]:
                min = n
        list[i], list[min] = list[min], list[i]
    print(list)

small(new_list)



