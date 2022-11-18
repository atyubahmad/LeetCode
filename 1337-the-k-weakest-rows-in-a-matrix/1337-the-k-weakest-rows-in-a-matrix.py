class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = sorted(range(len(mat)), key=lambda i: (mat[i], i))
        del rows[k:]
		
        return rows