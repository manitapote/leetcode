### Ways to sort dictionary
- OrderedDict class (may not be very good interms of performance)
- 

Strings can be sorted in list by different characters
in string. <br />
```
def select_second_character(word):
    return word[1]

sorted(words, key=select_second_character)
```

Difference between sort and sorted:<br />
string.sort()  => sorts in-place <br />
sorted(string) => returns the new view <br /><br />

sorted(dictionary) => return sorted keys<br />

```
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
view = people.items()
people[2] = "Elvis"
view
Result:
dict_items([(3, 'Jim'), (2, 'Elvis'), (4, 'Jane'), (1, 'Jill')])
```
The view returns the updated dictonary as well.
We can sort by using key function.
```
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

# Sort key
def value_getter(item):
    return item[1]


sorted(people.items(), key=value_getter)

# Or with a lambda function
sorted(people.items(), key=lambda item: item[1])
Result:
[(2, 'Jack'), (4, 'Jane'), (1, 'Jill'), (3, 'Jim')]
```

dictionary.get(key_name, default_value) => to get the value of key if present else return default value <br />
For sorting with dictionary: the list of dictionary sorting is efficient than one dictionary <br /> 
For lookups, dictionary is more efficient than list of dictionary. <br />

```
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

from operator import itemgetter
sorted(people.items(), key=itemgetter(1))
#This is faster compared to getting item with lambda function
```

