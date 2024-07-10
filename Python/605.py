from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        aux = 0 
        if n == 0: #if n is 0, then we can always place the flowers
            return True
        for i in range(len(flowerbed)): 
            #if the current position is empty and the previous and next positions are empty, then we can place a flower
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0): 
                flowerbed[i] = 1
                aux += 1
                if aux == n:
                    return True
        return False