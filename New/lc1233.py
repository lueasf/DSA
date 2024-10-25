class Solution:
    def removeSubfolders(self, folder):
        folder.sort()
        res = []

        for f in folder:
            if not res or not f.startswith(res[-1] + '/'):
            # si res est vide ou si f ne commence pas par res[-1] + '/'
                res.append(f)
        return res
