### Hashmap

Creation: my_dict = {}
- Time complexity = O(1)
- Space complexity = O(n)
  
Adding or updating entries: my_dict[key] = value
- Time Complexity = O(1), O(n) in worst case due to hash collisions or resizing
- Space complexity = O(1) for adding or updating single key-value pair

Accessing Values: value = my_dict[key]
- Time Complexity = O(1)
- Space complexity = O(1)

value = my_dict.get(key, default)
<br />

Deleting entries = del my_dict[key]
- Time: O(1) and O(n) in worst case
- Space: O(1)
  
my_dict.clear()

my_dict.pop(key, default)
- Remove akey-value pair and returns the value
- Returns default if key doesn't exist

Membership Checking: key in my_dict
- Time: O(1), O(n) in worst case due to hash collisions
- Space: O(1)

Iterating: for key in my_dict
- Time: O(n)
- Space: O(1)

for value in my_dict.values()
- Time complexity: O(n)
- Space complexity: O(1)

for key, value in my_dict.items()
- Time: O(n)
- Space: O(1)

Copying: new_dict = my_dict.copy()
- Time: O(n)
- Space: O(n)

Length: len(my_dict)
- Time: O(1)
- Space: O(1)

Default Value handling: my_dict.setdefault(key, default)
- Time: O(1), O(n) in worst case
- Space: O(1)

Updating: my_dict.update(another_dict)
- Time: O(n)
- Space: O(n)

Sorting by key: sorted(my_dict.items())
- Time: O(nlog(n)) Timsort
- Space: O(n)
