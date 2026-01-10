class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        s = list(s)
        front, back = 0, len(s)-1

        while front < back:
            if s[front] not in vowels: front += 1
            elif s[back] not in vowels: back -= 1
            else:
                s[front], s[back] = s[back], s[front]
                front += 1
                back -= 1
        
        return "".join(s)