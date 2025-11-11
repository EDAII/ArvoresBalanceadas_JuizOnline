from sortedcontainers import SortedList  # ✅ B-TREE

class MyCalendar:
    def __init__(self):
        self.calendar = SortedList()  # ✅ ÁRVORE BALANCEADA (B-tree)

    def book(self, start: int, end: int) -> bool:
        # Busca binária O(log n) na árvore balanceada
        idx = self.calendar.bisect_right((start, end))
        
        # Verifica sobreposição com evento anterior
        if idx > 0 and self.calendar[idx - 1][1] > start:
            return False
            
        # Verifica sobreposição com próximo evento
        if idx < len(self.calendar) and self.calendar[idx][0] < end:
            return False
            
        # Inserção balanceada O(log n)
        self.calendar.add((start, end))
        return True
