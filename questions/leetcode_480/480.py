from sortedcontainers import SortedList 

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList()  # ✅ ÁRVORE BALANCEADA
        result = []
        
        for i in range(len(nums)):
            # Inserção balanceada O(log k)
            window.add(nums[i])
            
            # Remoção balanceada O(log k)
            if len(window) > k:
                window.remove(nums[i - k])
            
            # Cálculo da mediana O(1) - elementos sempre ordenados
            if len(window) == k:
                if k % 2 == 1:
                    median = window[k // 2]  # Elemento do meio
                else:
                    median = (window[k // 2 - 1] + window[k // 2]) / 2
                result.append(median)
                
        return result
