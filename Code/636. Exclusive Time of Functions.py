class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        cum_time = [0 for i in range(n)]
        start_time = [None for i in range(n)]
        for log in logs:
            idstr, event, timestampstr = log.split(':')
            current_index = int(idstr)
            timestamp = int(timestampstr)
            if not stack:
                stack.append(current_index)
                start_time[current_index] = timestamp
            else:
                if event == "start":
                    previous_index = stack[-1]
                    cum_time[previous_index] += (timestamp - start_time[previous_index])
                    start_time[previous_index] = None
                    start_time[current_index] = timestamp
                    stack.append(current_index)
                elif event == "end":
                    stack.pop()
                    cum_time[current_index]  += (timestamp - start_time[current_index] + 1)
                    start_time[current_index] = None
                    if stack:
                        previous_index = stack[-1]
                        start_time[previous_index] = timestamp + 1
        return cum_time