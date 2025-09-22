class Solution(object):
    def maxWidthVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x_coords = sorted(set([p[0] for p in points]))
        max_width = 0
        for i in range(1, len(x_coords)):
            max_width = max(max_width, x_coords[i] - x_coords[i - 1])
        return max_width
    

if __name__ == '__main__':
    # You can test your code here
    solution = Solution()
    points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
    print(solution.maxWidthVerticalArea(points))