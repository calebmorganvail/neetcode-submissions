class Solution:
    def trap(self, heights: List[int]) -> int:
        """Returns the total amount of water that can 
        be traped between the bars. 

        Args:
            height: The list of non negative heights.
        
        Returns: 
            An integer as the amount of water than can be trapped.

        Time Complexity:

        Space Complexity:
      
        """ 
        area: int = 0

        l_flag = 0
        r_flag = 0
        i = 0
        while i < len(heights) - 1:
            
            r = i + 1
               
            if heights[r] <= heights[i]:
                l_flag = i

                r_flag = None
                for j in range(i + 1, len(heights)):
                    if heights[j] >= heights[i]:
                        r_flag = j
                        break
                    
                if r_flag is None:
                    r_flag = i + 1
                    for j in range(i + 2, len(heights)):
                        if heights[j] > heights[r_flag]:
                            r_flag = j

                area += ((r_flag- l_flag) - 1) * min(heights[l_flag], heights[r_flag])

                for t in range(l_flag + 1, r_flag):
                    area -= heights[t]
                
                i = r_flag

            else:
                i += 1
                
        return area
    
                    
                    


