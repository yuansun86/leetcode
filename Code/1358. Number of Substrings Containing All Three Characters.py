class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if not s:
            return 0
        record = {'a':0, 'b':0, 'c':0}
        record[s[0]] = 1
        slow, fast = 0, 0
        count = 0
        str_length = len(s)
        while slow < str_length:
            if record['a'] >= 1 and record['b'] >= 1 and record['c'] >= 1:
                count += str_length - fast
                ch = s[slow]
                record[ch] -= 1
                slow += 1
            else:
                fast += 1
                if fast >= str_length:
                    break
                ch = s[fast]
                record[ch] += 1
        return count