from collections import deque

a = ['v','a','i','b','h','a','v']
d = deque(a)

print(d)

# d.append('buccha')  # append at the last
d.appendleft('buccha') # append at the bignning

# d.pop() # remove from the end
d.popleft() #remove form the start
print(d)