#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Bonus: Can you do this in one pass?


nums=[10,15,3,7]
k=17

def sum_k(nums,k):
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            ans=nums[i]+ nums[j]
            if (ans == k):
                print('True')
                break

print(sum_k(nums,k))
