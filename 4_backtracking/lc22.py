# Given n pairs of parentheses, write a function 
# to generate all combinations of well-formed parentheses.

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

def generateParenthesis(n):
	def backtrack(left, right, s):
		if len(s) == n * 2:
			res.append(s)
			return 

		if left < n:
			backtrack(left + 1, right, s + '(')

		if right < left:
			backtrack(left, right + 1, s + ')')

	res = []
	backtrack(0, 0, '')
	return res