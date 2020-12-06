class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        cum_time = [0 for i in range(n)] # cumulative running time for each function
        start_time = [None for i in range(n)] # starting time for current running function
        for log in logs:
            idstr, event, timestampstr = log.split(':')
            current_index = int(idstr)
            timestamp = int(timestampstr)
            if not stack:
                # empty stack, only push to stack and update starting time
                stack.append(current_index)
                start_time[current_index] = timestamp
            else:
                if event == "start":
                    # push a new function, first shelf the old function
                    previous_index = stack[-1]
                    cum_time[previous_index] += (timestamp - start_time[previous_index]) # update cum_time of old function
                    start_time[previous_index] = None # reset starting time of old function
                    start_time[current_index] = timestamp # set the starting time of new function
                    stack.append(current_index) # push new function to stack
                elif event == "end":
                    stack.pop() # will always make a fair, so stack.pop() == current_index
                    cum_time[current_index]  += (timestamp - start_time[current_index] + 1) # update cum_time of old function
                    start_time[current_index] = None # reset starting time of old function 
                    if stack:
                        # if still something left on stack
                        previous_index = stack[-1] # peek the index
                        start_time[previous_index] = timestamp + 1 # set the starting time
        return cum_time