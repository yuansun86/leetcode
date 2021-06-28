class Solution:
    def candy(self, ratings: List[int]) -> int:
        heap = []
        for i, rating in enumerate(ratings):
            heapq.heappush(heap, (rating, i))
        res = [1] * len(ratings)
        while heap:
            rating, i = heapq.heappop(heap)
            if i - 1 >= 0 and ratings[i - 1] > ratings[i]:
                if res[i - 1] <= res[i]:
                    res[i - 1] = res[i] + 1
            if i + 1 < len(ratings) and ratings[i + 1] > ratings[i]:
                if res[i + 1] <= res[i]:

                    res[i + 1] = res[i] + 1
        return sum(res)