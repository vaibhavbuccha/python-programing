from collections import namedtuple
#  we create a refrence varible of the name tuple name courses which contains 2 names
a = namedtuple('courses', 'name, technology' )
#  here we assign the values to the name of the course nametuple.
s = a('data scientist', 'Python')
print(s) #print complete nametuple
print(s.name) #print only course name 

# use list to get a name tuple
# _make() :- This function is used to return a namedtuple() from the iterable passed as argument
li = a._make(['Django', 'Python'])
print(li)