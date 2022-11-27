class Solution:
    def numberOfArithmeticSlices(self, arr: List[int]) -> int:
        map_freq = [defaultdict(int)]
        ans = 0
        n = len(arr)
        for i in range(1,n):
            map_freq.append(defaultdict(int)) 
            for j in range(i):
                diff = arr[i] - arr[j]
                #print(i,j,map_freq,diff)
                sum = map_freq[j][diff]
                map_freq[i][diff] += sum+1
                ans += sum
        return ans