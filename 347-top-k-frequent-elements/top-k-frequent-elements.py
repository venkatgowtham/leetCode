class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freqMap = {}

        for i in nums:
            freqMap[i] = freqMap.get(i, 0) + 1
        
        counter = [[] for n in range(len(nums)+1)]

        for index, val in freqMap.items():
            counter[val].append(index)

        print(counter)
        ans = []
        i = len(counter)-1
        while i > 0:
            print("len" , len(counter[i]))
            if len(counter[i])>0:
                print(i)
                ans.extend(counter[i])
            
            if ans and len(ans) >= k:
                break
            i -=1
        return ans