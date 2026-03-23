class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        value = {}

        for s in strs:
            count = [0] * 26

            for ch in s:
                index = ord(ch) - ord('a')
                #print(index)
                count[ord(ch) - ord('a')] += 1

            if tuple(count) in value:
                value[tuple(count)].append(s)
            else:
                value[tuple(count)] = [s]
        
        return value.values()

        