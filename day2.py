#Given an array of integers, return a new array such that each element at
#index i of the new array is the product of all the numbers in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
#If our input was [3, 2, 1], the expected output would be [2, 3, 6].

#Follow-up: what if you can't use division?


lst=[1,2,3,4,5]
new_lst=[]


for i in range(len(lst)):
    num=1
    #print(i)
    temp=lst.copy()
    #print(temp)
    temp.pop(i)
    for j in temp:
        #print('j: ' + str(j))
        num=num*j
        #print('num:' + str(num))
    new_lst.append(num)
    #print(new_lst)
print(new_lst)
