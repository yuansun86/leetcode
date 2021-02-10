"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(employee, emap):
            return emap[employee].importance + sum(dfs(eid, emap) for eid in emap[employee].subordinates)
        emap = {e.id:e for e in employees}
        return dfs(id, emap)
        