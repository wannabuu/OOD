import itertools

arrOfNum = input("Enter Your List : ")
lst = arrOfNum.split()

#convert string to int
for i in range(len(lst)):
    lst[i] = int(lst[i])

#3SUM
if len(lst) >= 3:
    result = []
    for i in range(0, len(lst)-2):
        for j in range(i + 1, len(lst)-1):
            for k in range(j + 1, len(lst)):
                if sum([lst[i], lst[j], lst[k]]) == 5: 
                    result.append([lst[i], lst[j], lst[k]])
    
    new_res = []
    for elem in result:
        if elem not in new_res:
            new_res.append(elem)
    resultf = {tuple(sorted(i)) : i for i in new_res}.values()
    
    print(list(resultf))
else:
    print("Array Input Length Must More Than 2")