# variables in python

## common variables datatypes are
- integer  => ```12```
- float    => ```12.00```
- boolean  => ```True/1 , False/0```
- string   => ```'vaibhav'```
- complex  => ```10+j```
---
## String
---
> string in python are immutable means we can't change the value once we assign in a variable.
```py
name = "vaibhav jain"
# we assign value in name variable if we want to change the value of any index than python won't allow us to do that for example
name[0:3] = abc  # this code give error
```
> string in python represented as object means we can use indexing in string.
```py
name = "vaibhav"
name[0] # -> v
name[0:3]  # -> vai
name[:4]  # -> vaib
name[-1] # -> v
len(name) # 7
```
> *Note:-* Len() is use words of the string.
---
## List
---
> List in Python is special datatype which helps in holding multiple data in single variable. 
```py
nums = [1,2,34,5,6]
```
> List values are accessible using indexing similar as string.
```py
nums = [1,2,34,5,6]
print(nums[-1]) # 6
print(nums[-3]) # 34
print(nums[2:]) # 5,6
```
> List is mutable datatype therefor we can change the value of any index of the string.
```py
nums = [1,2,34,5,6]
nums[0] = 5
print(nums) # [5,2,34,5,6]
```
> List contains can take any type of data. it is not required to put similar datatypes.
```py
nums = ["vaibhav" , 8, "jain", True, 19.89]
```
> Len() is used for count length of the list
```py
nums = [1,2,3,45,6]
print(len(nums)) # 5
```
> Only Addition is allowed between 2 Lists.
```py
nums1 = [1,2,3]
nums2 = [1,2,3]
print(num1+num2) # [1,2,3,1,2,3]
```
> There are n number of function we can perform with list which is predefined in python some of them are ```insert , append, remove, clear``` etc.

1. _**append :-**_ take on parameter as a value and append at the end of list
```py
nums1 = [1,2,3,45,5,45]
nums1.append(22)
print(nums1) #[1, 2, 3, 45, 5, 45, 22]
```

2. _**clear :-**_ Clear all elements of the list
```py
nums1 = [1,2,3,45,5,45]
nums1.clear()
print(nums1) #[]
```

3. _**copy :-**_ return copy of the list.
```py
nums1 = [1,2,3,45,5,45]
print(nums1.copy()) #[1, 2, 3, 45, 5, 45]
```

4. _**count :-**_ take one value as param and return count of its presence.
```py
nums1 = [1,2,3,45,5,45]
print(nums1.count(45)) #2
```

5. _**index :-**_ Index takes value as argument and return its index
```py
nums1 = [1,2,3,45,5,45]
print(index(45)) # 3 always return 1st presence.
```

6. _**pop :-**_ pop takes an index as argument and remove it from list.
```py
num1 = [1,2,3,45,6,7]
num1.pop(2)
print(num1) # [1,2,45,6,7]
```

7. _**remove :-**_ remove takes value as argument and remove it from list.
```py
num1 = [1,2,34,56,5]
num1.remove(1)
print(num1) # [2,34,56,5]
```

8. _**sort :-**_ Sort list in assending/descending order.
```py
nums1.sort()
print(nums1)

# we can also extend sort in many ways
#  sort accept 2 params sort(reverse=True, key=myFunc)
```
---
## Tuples
---
> Tuples is also a special datatype in python which is quite similar like list but it is written in paranthesis ```()``` 
```py
tup = (1,2,34,5)
```

> Tuples are immutable means we can't change the value of the tuple.

> Tuple supports only 2 functions 

1. _**index :-**_ Index takes value as argument and return its index
```py
nums1 = (1,2,3,45,5,45)
print(index(45)) # 3 always return 1st presence.
```
2. _**count :-**_ take one value as param and return count of its presence.
```py
nums1 = (1,2,3,45,5,45)
print(nums1.count(45)) #2
```
> **ADVANTAGE OF TUPLE :~** Itration of tuple is faster than list.

---
## Sets
---
> Sets are another special datatype in python use for store multiple values. sets are initialise in ```{}```.
```py
s = {1,24,56,78}
```

> Sets don't contain any sequence so they are not accessible by index or they won't contain index.

> sets are work on hash so they process faster than list.

> sets doesn't contain duplicate values.
