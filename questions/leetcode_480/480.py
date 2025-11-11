from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList()
        result = []
        
        for i in range(len(nums)):
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i - k])  # O(log k) - árvore balanceada!
            
            if len(window) == k:
                # Acesso por índice em O(1) - mantido ordenado
                median = (window[k//2] + window[(k-1)//2]) / 2
                result.append(median)
                
        return result
