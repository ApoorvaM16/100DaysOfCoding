class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == '' or len(strs) == 1:
            return [strs]
        res, strDict = [],{}
        for i in strs:
            j = ''.join(sorted(i))
            if j in strDict:
                strDict[j].append(i)
            else:
                strDict[j] = [i]
        print(strDict)
        for key, val in strDict.items():
            res.append(val)
        return res