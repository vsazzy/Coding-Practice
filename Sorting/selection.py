#Select min and swap

def selection(lst, size):
    for i in range(size):
        min=i
        for j in range(i+1, size):
            if lst[j]<lst[min]:
                min=j
        lst[i],lst[min]=lst[min],lst[i]
    print(lst)

selection([3,2,1],len([3,2,1]))