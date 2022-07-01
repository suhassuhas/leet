class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse = True)
        totalSize = truckSize
        maxUnits = 0
        index  = 0
        for index in range(len(boxTypes)):
            print(index)
            box = boxTypes[index][0]
            if box <= totalSize:
                maxUnits += (boxTypes[index][0]*boxTypes[index][1])
                index += 1
                totalSize -=box
            else:
                maxUnits += (totalSize) * boxTypes[index][1]
                totalSize = 0
                break
        return maxUnits
                
        # boxTypes.sort(key=lambda x:x[1],reverse=True)
        # print(boxTypes)
        # boxCount = truckSize
        # totalScore = 0
        # n=len(boxTypes)
        # for i in range(n):
        #     #print(totalScore,boxCount)
        #     box = boxTypes[i]
        #     if box[0]<boxCount:
        #         totalScore += (box[1]*box[0])
        #         boxCount-=box[0]
        #     elif box[0]==boxCount:
        #         totalScore += (box[1]*box[0])
        #         boxCount-=box[0]
        #         break
        #     else:
        #         optimalBoxes = boxCount
        #         totalScore += box[1]*optimalBoxes
        #         break
        # return totalScore