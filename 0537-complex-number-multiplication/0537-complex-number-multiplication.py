class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        fR,fC = num1.split("+")
        fR = int(fR)
        fC = int(fC.split("i")[0])
        
        sR,sC = num2.split("+")
        sR = int(sR)
        sC = int(sC.split("i")[0])
        
        real1 = (fR*sR)
        mixed1 = (fR*sC)
        mixed2 = (fC*sR)
        complex1 = (fC*sC)
        
        real_ = real1 - complex1
        complex_ = mixed1 + mixed2
        return "%d+%di"%(real_,complex_)        
        