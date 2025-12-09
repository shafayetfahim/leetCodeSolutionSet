class Solution:
    def reverse(self, x: int) -> int:
        bits = 32
        int_min = -2 ** (bits - 1)
        int_max = 2 ** (bits - 1) - 1

        if x == 0: return 0
        elif x < int_min: return 0
        elif x > int_max: return 0

        r = str(x)[::-1]
        n = False
        if x < 0: 
            n = True
            r = r[:len(r)-1:]
        r = r.lstrip("0")

        if n: return -1*int(r) if -1*int(r) > int_min else 0
        return int(r) if int(r) < int_max else 0
        