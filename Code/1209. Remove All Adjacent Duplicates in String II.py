class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        str_copy = s
        while True:
            length = len(str_copy)
            has_remove = False
            count = 0
            for i in range(length):
                if i == 0 or str_copy[i] != str_copy[i-1]:
                    count = 1
                else:
                    count += 1

                if count == k:
                    str_copy = str_copy[:i-k+1] + str_copy[i+1:]
                    has_remove = True
                    break
            if not has_remove:
                return str_copy
            