class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        result = []
        for num in nums:
            result.append(sorted_nums.index(num))
        return result
    
if __name__ == '__main__':
    # You can test your code here
    solution = Solution()
    nums = [7,7,7,7]
    print(solution.smallerNumbersThanCurrent(nums))