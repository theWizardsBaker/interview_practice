# Daily Interview Pro Solution
# parentheses checker
class Solution:
  def isValid(self, s):
  	opener = ['[', '(', '{']
  	closer = [']', ')', '}']
  	found = []
  	valid = True
  	for char in s:
  		if char in opener:
  			found.append(opener.index(char))
  		if char in closer:
  			openTag = found.pop()
  			if openTag != closer.index(char):
  				valid = False
  				break
  	return valid and not bool(found)

# Test Program
s = "()(){(())"
# should return False
print(s, Solution().isValid(s))

s = ""
# should return True
print(s, Solution().isValid(s))

s = "([{}])()"
# should return True
print(s, Solution().isValid(s))

s = "([{[]}])()"
# should return True
print(s, Solution().isValid(s))

s = "([[{{"
# should return True
print(s, Solution().isValid(s))
