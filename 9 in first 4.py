#PF-Prac-4
def find_nine(nums):
	if(9 in nums and nums.index(9)<4):
		return True
	return False	
   
nums=[1,7,4,5,0]
print(find_nine(nums))
