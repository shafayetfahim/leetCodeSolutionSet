class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xz = abs(z - x)
        yz = abs(z - y)
        if xz < yz: return 1
        elif xz > yz: return 2
        return 0