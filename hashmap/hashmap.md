### Hashmap

Creation: my_dict = {}
- Time complexity = O(1)
- Space complexity = O(n)

<br />
Adding or updating entries = my_dict[key] = value
- Time Complexity = O(1), O(n) in worst case due to hash collisions or resizing
- Space complexity = O(1) for adding or updating single key-value pair

<br />
Accessing Values: value = my_dict[key]
- Time Complexity = O(1)
- Space complexity = O(1)

<br />
value = my_dict.get(key, default)
<br />

Deleting entries = del my_dict[key]
- Time: O(1) and O(n) in worst case
- Space: O(1)
<br />
my_dict.clear()
<br />
my_dict.pop(key, default)
- Remove akey-value pair and returns the value
- Returns default if key doesn't exist

<br />
Membership Checking: key in my_dict
- Time: O(1), O(n) in worst case due to hash collisions
- Space: O(1)

<br />
Iterating: for key in my_dict
- Time: O(n)
- Space: O(1)
<br />
for value in my_dict.values()
- Time complexity: O(n)
- Space complexity: O(1)
<br />
for key, value in my_dict.items()
- Time: O(n)
- Space: O(1)
<br />
Copying: new_dict = my_dict.copy()
- Time: O(n)
- Space: O(n)
<br />
Length: len(my_dict)
- Time: O(1)
- Space: O(1)
<br />
Default Value handling: my_dict.setdefault(key, default)
- Time: O(1), O(n) in worst case
- Space: O(1)
<br />
Updating: my_dict.update(another_dict)
- Time: O(n)
- Space: O(n)
<br />
Sorting by key: sorted(my_dict.items())
- Time: O(nlog(n)) Timsort
- Space: O(n)
