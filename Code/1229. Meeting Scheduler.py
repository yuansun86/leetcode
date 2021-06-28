class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        i = 0 
        j = 0
        while i < len(slots1) and j < len(slots2):
            first = slots1[i]
            second = slots2[j]
            if first[0] <= second[0]:
                # case 1
                if second[0] < first[1]:
                     # has interval
                    interval = min(first[1], second[1]) - second[0]
                    if interval >= duration:
                        return[second[0], second[0] + duration]
                    else:
                        if first[1] <= second[1]:
                            i += 1
                        else:
                            j += 1
                else:
                     # no interval
                    i += 1
            else:
                # case 2
                if first[0] < second[1]:
                    # has interval
                    interval = min(second[1], first[1]) - first[0]
                    if interval >= duration:
                        return [first[0], first[0] + duration]
                    else:
                        if second[1] <= first[1]:
                            j += 1
                        else:
                            i += 1
                else:
                    j += 1
        return []
                