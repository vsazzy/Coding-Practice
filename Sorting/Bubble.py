#Bubble Sort: swap adjacent elements

def bubble(lst,n):
    for i in range(n):
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                lst[j], lst[j+1]=lst[j+1],lst[j]
    print(lst)

bubble([3,2,1],len([3,2,1]))