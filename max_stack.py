class MaxStack:
  def __init__(self):
    # Fill this in.
    self.stack = []
    self.max_stack = []

  def push(self, val):
    # Fill this in.
    self.stack.append(val)
    if len(self.max_stack) == 0 or val >= self.max_stack[-1]:
      self.max_stack.append(val)

  def pop(self):
    # Fill this in.
    if self.stack[-1] == self.max_stack[-1]:
      self.max_stack.pop()

    return self.stack.pop()

  def max(self):
    # Fill this in.
    return self.max_stack[-1]

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print s.max()
# 3
s.pop()
s.pop()
print s.max()
# 2
s = MaxStack()
s.push(4)
s.push(2)
print s.max()
s.push(14)
s.push(1)
print s.max()
s.push(18)
print s.max()
s.pop()
s.pop()
print s.max()