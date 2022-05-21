class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def coinsum(target):
            if target in coins:
                return 1
            if target < 0:
                return -1
            consider = [c for c in coins if c < target]
            minpath = float('inf')
            for coin in consider:
                num = coinsum(target-coin)
                if num < 1:
                    continue
                minpath = min(minpath,1+num)
            return minpath if minpath != float('inf') else -1
        return coinsum(amount) if amount > 0 else 0
        