class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group anagrams into a hashmap
        anagramDict = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagramDict[sorted_word].append(word)
        return list(anagramDict.values())
            

        # traverse hashmap and return each group into subarrays of a  res array


        # anagram_map = defaultdict(list)
        
        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        #     anagram_map[sorted_word].append(word)
        # return list(anagram_map.values())
        