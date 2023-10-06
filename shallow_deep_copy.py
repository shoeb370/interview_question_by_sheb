#shallow copy
"""
A shallow copy is a type of copy operation in computer programming that creates a new object or data structure, but it does not create copies of the objects or elements contained within the original object. Instead, it copies references or pointers to those objects or elements. This means that changes made to the objects or elements within the original structure may also be reflected in the copied structure, as they both point to the same underlying objects.

The exact behavior of a shallow copy can vary depending on the programming language and data structures being used. In Python, for example, you can create a shallow copy of a list using the copy() method or the copy module's copy() function. Here's an example:
"""
import copy

original_list = [1, 2, 3, [4, 5]]
shallow_copy = copy.copy(original_list)

# Modify an element within the original list
original_list[3][0] = 99

print(original_list)   # Output: [1, 2, 3, [99, 5]]
print(shallow_copy)   # Output: [1, 2, 3, [99, 5]]


#Deep copy
"""
If one is a shallow copy, the other copy would typically be a deep copy. A deep copy is a type of copy operation in computer programming that creates a completely independent copy of an object or data structure, including all the objects and elements contained within it. Unlike a shallow copy, a deep copy ensures that changes made to the original object's elements are not reflected in the copied object, as they are entirely separate instances.

In Python, you can create a deep copy of an object using the copy module's deepcopy() function. Here's an example:
"""

import copy

original_list = [1, 2, 3, [4, 5]]
deep_copy = copy.deepcopy(original_list)

# Modify an element within the original list
original_list[3][0] = 99

print(original_list)   # Output: [1, 2, 3, [99, 5]]
print(deep_copy)      # Output: [1, 2, 3, [4, 5]]
