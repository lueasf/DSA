# Premier palindrom dans u tableau de str

class Solution:
    def pal(self, string):
        for i in range(len(string) // 2):
            if string[i] != string[-i - 1]:
                    return False
        return True
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            if self.pal(words[i]):
                return words[i]
        return ""