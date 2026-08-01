class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        greatest = max(candies)
        ans = []

        for candy in candies:
            if candy + extraCandies >= greatest:
                ans.append(True)
            else:
                ans.append(False)

        return ans