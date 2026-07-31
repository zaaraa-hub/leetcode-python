class Solution(object):
    def runningSum(self, nums):
        result = []
        running_sum = 0

        for num in nums:
            running_sum += num
            result.append(running_sum)

        return result