class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        outputString = []
        for i in range(len(order)):
            if order[i] in friends: outputString.append(order[i])
        return outputString


        