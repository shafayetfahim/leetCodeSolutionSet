class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            match operations[i]:
                case "C": record.pop()
                case "D": record.append(int(2 * record[-1]))
                case "+": record.append(int(record[-1] + record[-2]))
                case _: record.append(int(operations[i]))
        return sum(record)

        