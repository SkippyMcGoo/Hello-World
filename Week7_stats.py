lst = []

def mean(lst):
    if not lst:
        avg = 0
    else:
        avg =  sum(lst) / len(lst)
    return avg
def median(lst):
    med = 0
    lst.sort()
    mid = len(lst)//2
    if not lst:
        med = 0
    elif len(lst)%2!=0:
       med = lst[mid]
    elif len(lst)%2==0:
        med = (lst[mid - 1] + lst[mid])/2
    return med
def mode(lst):
    if not lst:
        mod = 0
    else:
        mod = max(set(lst), key=lst.count)
    return mod

average = mean(lst)
middle = median(lst)
most = mode(lst)
print("Average:", average)
print("Median:", middle)
print("Mode:", most)


    
