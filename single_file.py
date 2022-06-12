#problem_1:   (Single Number )
#python
class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result = result ^ i
        return result 

#java
"""
    class Solution {
    public int singleNumber(int[] nums) {
        int i;
        int result = 0;
        for (i=0; i< nums.length; i++){
            result = result ^ nums[i];
        }
        return result;
        
    }
}
"""

    
#problem_2: (Single Number II)
#problem_3: (Majority Element)
#problem_4: (Bitwise AND of Numbers Range)
#problem_5: (Counting Bits)
#problem_6: (Hamming Distance)
#problem_6: (Decode XORed Permutation)


    
