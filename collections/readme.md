# Collections in Python
-   Collectionsof datatypes
    - Main collections are following.
        1. List
        2. Tuple
        3. Set
        4. Dictornary

#### Specialised collection Datatypes

                    Nametuple
        ________________|_______________
        |                              |
    Chainmap                          deque

                    Counter
        ________________|_______________
        |                              |
    OrderedDict                     DefaultDict

                    UserDict
        ________________|_______________
        |                              |
    UserList                       UserString

        
## NameTuple()
> nametuple() returns a tuple with a named value for each element in the tuple.
- Example
```py
details = (name='vaibhav', course='python', course2='Django')
```
- It make Things easy we don't have get the index we can get value directly from the name.
> _make() :- This function is used to return a namedtuple() from the iterable passed as argument

## Deque()
> deque() pronounced as 'deck' is an optimised list to perform insertion and deleteion easily.