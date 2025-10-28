class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        currentRichest = 0
        for account in accounts:
            if sum(account) >= currentRichest: currentRichest = sum(account)
        return currentRichest