class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      #here we have to first take sorting of the array
      
        result=[]
        candidates.sort()
        
        def solve(index,curr_sum,subset):
          #give an base case like we are gouing in decreasing manner given sum =5 with each iteration it is deducting the element from sum
            if curr_sum==0 :
                result.append(subset.copy())
                return
            if curr_sum<0:
                return
              #this for loops checks if the first element is not repeating if repeats skip that elemnt
          
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                  #aPPEND THE value in result array
              
                subset.append(candidates[i])
              #deduct the a[i] element from curr_sum
                solve(i+1,curr_sum-candidates[i],subset)
                subset.pop()

     # dont foget that solve give the given sum not 0 as is going backwords
            
        solve(0,target,[])
        return result

        
