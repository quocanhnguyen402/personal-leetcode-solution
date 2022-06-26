/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    var result = new Array(nums.length);
    var golbal_max = 0;

    for (let i = 0; i < nums.length; i++) {
        const value = nums[i];
        var max_len = 1;
        for (let j = 0; j < i; j++) {
            const value_before = nums[j];
            if(value > value_before){
                max_len = Math.max(max_len,result[j] + 1);
            }
        }
        result[i] = max_len;
        golbal_max = Math.max(golbal_max,result[i]);
    }
    
    return golbal_max;
};