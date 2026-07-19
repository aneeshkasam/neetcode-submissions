class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];
        //fill prefix
        for(int i = 0; i < nums.length; i++)
        {
            if(i == 0)
            {
                prefix[i] = 1;
            }
            else
            {
                prefix[i] = prefix[i-1] * nums[i-1];
            }
        }

        //fill suffix
        for(int i = nums.length - 1; i >=0; i--)
        {
            if(i == nums.length-1)
            {
                suffix[i] = 1;
            }
            else
            {
                suffix[i] = suffix[i+1] * nums[i+1];
            }
        }

        int[] output = new int[nums.length];
        //fill output
        for(int i = 0; i < nums.length; i++)
        {
            output[i] = prefix[i] * suffix[i];
        }
     return output;
    }
}  
