class Solution(object):
    def largestAltitude(self, gain):
        altitude = 0
        highest = 0

        for num in gain:
            altitude += num

            if altitude > highest:
                highest = altitude

        return highest