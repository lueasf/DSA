# Container with most water : Facebook & Google

# il y un diagramme baton et on doit trouver les batons qui forment la plus grande aire.
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49


def maxArea(height):
    aire_max = 0
    l , r = 0 , len(height) -1
    while l<r:
        aa = (min(height[l],height[r]))*(r-l)
        aire_max = max(aire_max, aa)
        if height[l] < height[r]:
            l += 1
        else :
            r -= 1
    return aire_max
print(maxArea([2,6,1,5,4]))