class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        count = [0] * 5
        index = {'c':0, 'r':1, 'o':2, 'a':3, 'k':4}
        res = 0
        for letter in croakOfFrogs:
            if letter == 'c':
                count[0] += 1
                res = max(res, count[0])
            else:
                prev_index = index[letter] - 1
                self_index = index[letter]
                if count[self_index] + 1 <= count[prev_index]:
                    count[self_index] += 1
                else:
                    return -1
                if letter == 'k':
                    for i in range(5):
                        count[i] -= 1
        if sum(count) != 0:
            return -1
        return res