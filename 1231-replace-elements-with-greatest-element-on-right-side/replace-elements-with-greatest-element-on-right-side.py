class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        right_max= -1 
        n= len(arr)
        for i in range(n-1, -1, -1):
            temp = arr[i]
            arr[i] = right_max
            right_max = max(temp, right_max)
        return arr    
        