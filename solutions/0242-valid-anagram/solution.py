class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) or set(s) != set(t):
            return False
        
        sHash = dict()
        tHash = dict()
        for sChar in s:
            sHash[sChar] = sHash.get(sChar, 0) + 1
        for tChar in t:
            tHash[tChar] = tHash.get(tChar, 0) + 1
        
        return all([sItem == tItem for sItem, tItem in zip(sHash.items(), tHash.items())])
        
