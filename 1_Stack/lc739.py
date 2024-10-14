
# Daily Temperatues : Facebook
class Solution:
    def dailyTemperatures(self, temperatures):
        output = [ 0 for i in range(len(temperatures))]
        stack = [] # pair [temp, index]
        for i, t in enumerate(temperatures): # i index, t temp[i]
            while stack and t > stack[-1][0] : # tant que la pile est pleine et t est superieur a la temp du dernier elemnt
                stackT, stackInd = stack.pop()
                output[stackInd] = i - stackInd
            stack.append([t,i])
            
        return output