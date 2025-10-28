class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        currentRichest = 0
        for account in accounts:
            wealth = sum(account)
            if wealth > currentRichest: currentRichest = wealth
        return currentRichest