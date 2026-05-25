from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)

        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord(char)-ord('a')] += 1
            groups[tuple(freq)].append(string)
        
        return groups.values()


        
