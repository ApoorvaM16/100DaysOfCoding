class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
#         2 steps: 1.find the capacity      2. call the function for no.of days
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = low + (high-low)//2
            no_of_days = self.noOfDays(weights,mid)
            if no_of_days <= days:
                high = mid -1
            else:
                low = mid+1
        return low
    
    
    def noOfDays(self,weights,capacity):
        days, load = 1, 0
        for i in weights:
            if load + i > capacity:
                days +=1
                load = i
            else:
                load +=i
        return days
        