class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude, current_altitude = 0, 0
        for g in gain:
            current_altitude += g
            max_altitude = max(current_altitude, max_altitude)
        return max_altitude

        