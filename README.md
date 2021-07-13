# Game-A-Thon
This repository is for Game-A-Thon (Task 2) held on 12th July 2021.
## Name: Om Rachalwar
### Problem Statement 1: 
***Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.***

**TestCases:**
```
    array123([1, 1, 2, 3, 1]) → True
    array123([1, 1, 2, 4, 1]) → False
    array123([1, 1, 2, 1, 2, 3]) → True
```
           
My Approach:
* Creating Function named array123().
* Using if statement to confirm size of array is greater than 2.
* iterating with length-2.
* using i+1 and i+2 in the loop.
```python
if len(nums)>2:
    for i in range(len(nums)-2):
      if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
```

### Problem Statement 2: 
***Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.***

**TestCases:**
```
    array_front9([1, 2, 9, 3, 4]) → True
    array_front9([1, 2, 3, 4, 9]) → False
    array_front9([1, 2, 3, 4, 5]) → False
```		

My Approach:
* Creating Function named array_front9().
* To check first 4 elements, end the loop at 4.
```python
end=len(nums)
  if end>4:
    end=4
 ```
* Looping over index [0,1,2,3], till 9 is found.
```python
for i in range(end):
    if nums[i]==9:
```

### Problem Statement 3: 
***Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.***

**TestCases:**
```
string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
```
My Approach:
* Creating Function named string_match().
* Determining which string is shorter.
```python
  shorter = min(len(a), len(b))
  count = 0
```
* Looping i over every substring starting spot.
* Using length-1 here, and using str[i+1] in the loop.
```python
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1
```

### Problem Statement 4: 
***You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.***

**TestCases:**
```
caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0
```
My Approach:
* Creating Function named caught_speeding().
* Fulfilling the given conditions with the use of if,elif,else statements.
```python
  if  is_birthday and speed<=65:
    return 0
  elif is_birthday and 65<speed<=85:
    return 1
  elif speed<=60:
    return 0
  elif 60<speed<=80:
    return 1
  else:
    return 2
 ```
 
 
 (All the problem statements used in this repository are taken from CodingBat)
