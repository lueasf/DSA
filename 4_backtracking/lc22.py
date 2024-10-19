# Generate Parentheses : Amazon

# Given n pairs of parentheses, write a function 
# to generate all combinations of well-formed parentheses.

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# FAV

# BYME
def generateParenthesis(n):
	def backtrack(s,n, comp1, comp2, output):
		if len(s) == 2*n:
			output.append(s)
			return
		if comp1 < n:
			backtrack(s+"(", n, comp1+1, comp2, output)
		if comp2 < comp1:
			backtrack(s+")", n, comp1, comp2+1, output)
	
	output = []
	backtrack("", n, 0, 0, output)
	return output