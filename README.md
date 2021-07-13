# Game-A-Thon
This repository is for Game-A-Thon (Task 2) held on 12th July 2021.
# Name: Om Rachalwar 
# **Problem Statement 1: Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.**

**TestCases:**

           array123([1, 1, 2, 3, 1]) → True,

           array123([1, 1, 2, 4, 1]) → False.
           
           array123([1, 1, 2, 1, 2, 3]) → True.
           
My Approach:
* Creating Function.
* Using if statement to confirm size of array is greater than 2.
* iterating with length-2.
* using i+1 and i+2 in the loop.

		if len(nums)>2:
    		  for i in range(len(nums)-2):
      		    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
		    
		 

# **Problem Statement 2: Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.**

**TestCases:**
			
		array_front9([1, 2, 9, 3, 4]) → True
	
		array_front9([1, 2, 3, 4, 9]) → False
	
		array_front9([1, 2, 3, 4, 5]) → False
		
My Approach:
* Creating Function named array_front9.
* To check first 4 elements, end the loop at 4.

		end=len(nums)
  		if end>4:
   		  end=4
* Looping over index [0,1,2,3], till 9 is found.

		for i in range(end):
		   if nums[i]==9:

