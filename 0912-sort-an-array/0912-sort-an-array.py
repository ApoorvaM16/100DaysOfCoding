def merge(arr, low, mid, high):
    left, temp = low, []
    right = mid + 1
    while left <= mid  and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left +=1
        else:
            temp.append(arr[right])
            right +=1
    while left<=mid:
        temp.append(arr[left])
        left +=1
    while right <= high:
        temp.append(arr[right])
        right +=1
    for i in range(low, high+1):
        arr[i] = temp[i-low]
        
    # return arr, no need of return
    
def mergeSort(arr, low,high):
    if low >=high:
        return
    mid = (low + high)//2
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    merge(arr, low, mid, high)
    
    # return arr


class Solution:
   
    
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Merge sort best and worst case: O(nlogn)

        mergeSort(nums,0,len(nums)-1)
        return nums
    
    
    
#   Selection sort code: TC-O(n**2)
        # n = len(nums)
        # for i in range(len(nums)-1):
        #     minVal = i
        #     for j in range(i+1,len(nums)):
        #         if nums[j] < nums[minVal]:
        #             minVal = j
        #     nums[i], nums[minVal] = nums[minVal], nums[i]
        # return nums

    
    
    
#  Bubble sort best case TC:O(n), worst case TC: O(n**2), SC: O(1)
        # n, swapped = len(nums),0
        # for i in range(1,n):
        #     for j in range(0,n-i):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        #             swapped = 1
        #     if not swapped:
        #         break
        # return nums
                
        
# insertion sort best case TC:O(n), worst case TC: O(n**2), SC: O(1)



        # n = len(nums)
        # for i in range(n):
        #     j = i
        #     while j > 0 and nums[j-1] > nums[j]:
        #         nums[j], nums[j-1] = nums[j-1], nums[j]
        #         j -=1
        # return nums
        
   
    



