# palindrom phrase :
# Input: s = "A man, a plan, a canal: Panama"
# Output: true

#BYME
def isPalindrome(s):
    s = s.lower()
    new = ""
    for i in s:
        if i.isalnum(): 
            new += i
    for i in range(len(new)):
        if (new[i] != new[-i -1]):
            return False
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))