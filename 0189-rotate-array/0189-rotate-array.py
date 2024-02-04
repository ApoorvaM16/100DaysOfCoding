class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # if n ==2 and k% 2 != 0:
        #     nums[:] = nums[::-1]
        #     return
        # elif n ==2 and k%2 ==0:
        #     return
        # res = [0] * n
        # res[:k] = nums[n-k:]
        # res[k:] = nums[:n-k]
        # nums[:] = res

        # 2 pointer
        # j = n - 1
        # for i in range(n):
        #     if k>0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         j -=1
        #         k-=1

        # reversal

        # if k > n and n ==2:
        #     nums[:] = nums[::-1]
        #     return
        # nums[:] = nums[::-1]
        # nums[:k] = nums[:k][::-1]
        # nums[k:] = nums[k:][::-1]



#   O(n) and space=O(n)
        # res = [0]*n
        # for i in range(n):
        #     if i+k <n:
        #         res[i+k] = nums[i]
        #     else:
        #         res[(i+k) % n] = nums[i]
        # nums[:] = res

        # in-place reversing/ two pointers
        # check if k > len of array
        # k=k%n
        # i, j = 0, n-1
        # while i <j:
        #     nums[i],nums[j] = nums[j], nums[i]
        #     i, j =i+1, j-1
        # # print(nums)
        # i,j = 0, k-1 
        # while i <j:
        #     nums[i],nums[j] = nums[j], nums[i]
        #     i, j =i+1, j-1
        # # print(nums)
        # i,j = k, n-1 
        # while i <j:
        #     nums[i],nums[j] = nums[j], nums[i]
        #     i, j =i+1, j-1


        


        k = k%n
        nums[:] = nums[::-1]
        nums[:]= nums[:k][::-1]+nums[k:][::-1]








        
            