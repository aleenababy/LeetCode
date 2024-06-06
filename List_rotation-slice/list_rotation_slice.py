
"""List Rotation: Slice
22 min
For our first problem, we would like to “rotate” a list, or move elements forward in a list by a number of spaces, k.

Elements at the greatest index will “wrap around” to the beginning of the list.

list = ['a', 'b', 'c', 'd', 'e', 'f']
rotate(list, 0)
# ['a', 'b', 'c', 'd', 'e', 'f']
rotate(list, 1)
# ['f', 'a', 'b', 'c', 'd', 'e']
rotate(list, 3)
# ['d', 'e', 'f', 'a', 'b', 'c']

Clarifying Questions:

Are there constraints on time or space efficiency?
Nope! Just solve the problem.
Should I account for negative inputs?
The rotation input will always be positive.
What if the rotation is greater than the list length?
Continue wrapping!
The “rotated” list would be the same as the original when k is equal to the length."""

def rotate(my_list, num_rotations):
  if num_rotations == len(my_list):
      return my_list
  else:
    new_list = my_list
    for i in range(num_rotations):
        new_list.insert(0, new_list[-1])
        new_list = new_list[:-1]
  return new_list

def rotate(l, k):
  for i in range(k):
    l.insert(0, l.pop())
  return l

def rotate_alternative(lst, degree):
  rotation = degree % len(lst)
  return lst[-rotation:] + lst[:-rotation]


def rev(lst, low, high):
  while low < high:
    lst[low], lst[high] = lst[high], lst[low]
    high -= 1
    low += 1
  return lst

def rotate(my_list, num_rotations):
  # first half
  rev(my_list, 0, num_rotations - 1)

  # second half
  rev(my_list, num_rotations, len(my_list) - 1)

  # whole list
  rev(my_list, 0, len(my_list) - 1)
  return my_list