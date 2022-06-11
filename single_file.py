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
