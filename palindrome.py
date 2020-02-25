# Daily Interview Pro Solution
# Longest Substring
class Solution:
	def longestPalindrome(self, s):
		# Fill this in.
		longest_palindrome = {}
		string_len = len(s)
		# go through each letter
		for ind in range( string_len ):
			match = False
			palindrome_ind = [ind, ind]
			# print "looking at " + s[ind]
			# walk backwards over the string
			# for rng_ind in range(string_len - 1, ind -1, -1):
			rng_ind = string_len - 1
			while rng_ind >= ind:
				# return if we meet in the middle (odd number)
				if palindrome_ind[0] == rng_ind or rng_ind == ind:
					palindrome_ind[0] = ind
					break
				# check if the last index is equal to our current
				if s[palindrome_ind[0]] == s[rng_ind]:
					palindrome_ind[0] += 1
					if not match:
						palindrome_ind[1] = rng_ind
						match = True
					rng_ind -=1
				# if we're in matching and the next
				# char doesn't match, we cannot have a palindrome
				elif match:
					match = False
					palindrome_ind[0] = ind
				else:
					rng_ind -= 1
					# break
			palindrome_len = (palindrome_ind[1] + 1) - ind
			# check for min palindrome (3 chars)
			if match and palindrome_len >= 3:
				# print  ind, palindrome_len, s[ind:ind+palindrome_len]
				if palindrome_len in longest_palindrome:
					longest_palindrome[palindrome_len].append(s[ind:ind+palindrome_len])
				else:
					longest_palindrome[palindrome_len] = [s[ind:ind+palindrome_len]]
		return longest_palindrome


# Test program
print(str(Solution().longestPalindrome('bananna')))
print(str(Solution().longestPalindrome('tracecars')))
text1 = "babcbabcbaccba"
print(str(Solution().longestPalindrome(text1)))

text2 = "abaaba"
print(str(Solution().longestPalindrome(text2)))

text3 = "abababa"
print(str(Solution().longestPalindrome(text3)))

text4 = "abcbabcbabcba"
print(str(Solution().longestPalindrome(text4)))

text5 = "forgeeksskeegfor"
print(str(Solution().longestPalindrome(text5)))

text6 = "caba"
print(str(Solution().longestPalindrome(text6)))