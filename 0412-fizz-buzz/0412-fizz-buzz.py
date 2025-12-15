class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [""]*n
        for i in range(1, n+1):
            div3 = False
            div5 = False
            if i%3 == 0: div3 = True
            if i%5 == 0: div5 = True
            if div3 and div5: answer[i-1] = "FizzBuzz"
            elif div3: answer[i-1] = "Fizz"
            elif div5: answer[i-1] = "Buzz"
            else: answer[i-1] = str(i)
        return answer
        