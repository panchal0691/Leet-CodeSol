class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        K = celsius + 273.15
        F= celsius*1.8 + 32
        arr =[]
        arr.append(K)
        arr.append(F)
        return arr
        
