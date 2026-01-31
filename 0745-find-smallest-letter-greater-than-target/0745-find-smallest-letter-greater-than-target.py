from math import inf
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        min_distance = math.inf
        t = ord(target)
        goal_char = ''


        for letter in letters:
            distance = ord(letter) - t
            if distance > 0 and distance <= min_distance:
                goal_char = letter
                min_distance = distance
        
        if goal_char == "": return letters[0]
        return goal_char

            
        