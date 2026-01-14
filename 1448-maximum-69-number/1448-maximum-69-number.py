class Solution:
    def maximum69Number (self, num: int) -> int:
        n = list(map(int, str(num)))
        print(n)

        for i in range(len(n)):
            if n[i] == 6: 
                n[i] = 9
                break
        
        return int("".join(str(j) for j in n))