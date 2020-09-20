# nums = ["vaibhav" , 8, "jain", True, 19.89]
# print(nums)

nums1 = [1,2,3,45,5,45]
nums2 = [13,425,53,45,5]
# print(nums1+nums2) # addition is allow
# print(nums1 - nums2) # subtration not allow
# print(num1*num2)

#  so only addition is allow between 2 lists

# list methods

# append -> take on parameter as a value and append at the end of list
nums1.append(22)
print(nums1)

# clear -> remove all elements from the list
# nums1.clear()
# print(nums1)

# copy -> return copy of the list
# nums1.copy()
print(nums1.copy())

# count() -> accept one value and return the presence count of that value
print(nums1.count(45))

# index -> accept one value and return its index
print(nums1.index(45))

# insert -> it takes 2 params one is index on which you have to add the value and another one is value it self.
nums1.insert(3, 90)
print(nums1) 

# pop -> pop takes 1 params as index and remove value of that perticular index.
nums1.pop(2)
print(nums1)

# remove -> remove take one params as value and remove that specific value
nums1.remove(45)
print(nums1)

# reverse - >reverse is use to reverse the complete list
nums1.reverse()
print(nums1)

# sort -> sort list in assending order
nums1.sort()
print(nums1)

# we can also extend sort in many ways
#  sort accept 2 params sort(reverse=True, key=myFunc)