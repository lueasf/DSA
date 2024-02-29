# palindrom phrase :
# Input: s = "A man, a plan, a canal: Panama"
# Output: true

def isPalindrome(s):
    s = s.lower()
    res = ""
    for lettre in s:
        if lettre.isalnum():
            res += lettre
    
    for i in range(len(res)):
        if res[i] != res[-i -1]:
            return False
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))