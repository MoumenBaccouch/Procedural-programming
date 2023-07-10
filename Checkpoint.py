def dot_product(v1, v2):
  """
  Calculates the dot product of two vectors.

  Args:
    v1: A vector of IR.
    v2: A vector of IR.

  Returns:
    The dot product of v1 and v2.
  """

  ps = 0
  for i in range(len(v1)):
    ps += v1[i] * v2[i]
  return ps

def are_orthogonal(v1, v2):
  """
  Determines whether two vectors are orthogonal.

  Args:
    v1: A vector of IR.
    v2: A vector of IR.

  Returns:
    True if v1 and v2 are orthogonal, False otherwise.
  """

  ps = dot_product(v1, v2)
  return ps == 0

def insertion_sort(arr):
  """
  Sorts an array using the insertion sort algorithm.

  Args:
    arr: The array to be sorted.

  Returns:
    A sorted array.
  """

  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr

import dot_product
ps = dot_product([1, 2, 3], [4, 5, 6])

print(ps)  # 32
import dot_product

are_orthogonal = dot_product.are_orthogonal([1, 2, 3], [4, 5, 6])

print(are_orthogonal)  # True
import insertion_sort

arr = [1, 5, 3, 2, 4, 6]

sorted_arr = insertion_sort(arr)

print(sorted_arr)  # [1, 2, 3, 4, 5, 6]
