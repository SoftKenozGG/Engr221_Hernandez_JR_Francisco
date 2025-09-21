class Solution(object):
    def counPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num_set = set(nums)
        count = 0
        for i in range(len(num_set)):
            for j in range(i + 1, len(num_set)):
                if list(num_set)[i] + list(num_set)[j] < target:
                    count += 1
        return count
    
if __name__ == '__main__':
    # You can test your code here
    solution = Solution()
    nums = [-6,2,5,-2,-7,-1,3]
    target = -2
    print(solution.counPairs(nums, target))