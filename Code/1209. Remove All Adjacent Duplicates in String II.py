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


# Solution use a stack to keep the current count of character. If found k same characters, rewind i to i - k + 1, and rebuild string
# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         sb = s
#         counts = []
#         i = 0
#         while i < len(sb):
#             if i == 0 or sb[i] != sb[i-1]:
#                 counts.append(1)
#                 i += 1
#             elif counts[-1] == k - 1:
#                 counts.pop()
#                 sb = sb[:i-k+1] + sb[i+1:]
#                 i = i - k + 1
#             else:
#                 counts[-1] = counts[-1] + 1
#                 i += 1
#         return sb
            