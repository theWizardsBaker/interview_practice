from collections import Counter

def singleNumber(nums):
	found = Counter()
	for num in nums:
		found[num] += 1
	for num, occurance in found.items():
		if occurance == 1: return num
	return "All numbers are duplicates!"

print singleNumber([4, 3, 2, 4, 1, 3, 2])
print singleNumber([4, 4, 4, 4, 4, 4])
print singleNumber([4, 3, 2, 4, 1, 3, 2, 1, 2, 3, 4, 6])
# 1