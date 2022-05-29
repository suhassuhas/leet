class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        if num == 1:
            return [1,2]
        
        def find_closest_pair(n):
            sqrtn = math.sqrt(n)
            print(sqrtn)
            closet_pair = [float("inf"),float("-inf")]
            for i in range(1,math.floor(sqrtn)+1):
                if n % i == 0:
                    j = n // i
                    diff = abs(i-j)
                    diff_clos = abs(closet_pair[0]-closet_pair[1])
                    if diff < diff_clos:
                        closet_pair = [i,j]
            return closet_pair
        first_closest_pair = find_closest_pair(num+1)
        #print(first_closest_pair)
        second_closest_pair = find_closest_pair(num+2)
        #print(second_closest_pair)
        if abs(first_closest_pair[0]-first_closest_pair[1]) < abs(second_closest_pair[0]-second_closest_pair[1]):
            return first_closest_pair
        return second_closest_pair