/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxProduct = function(nums) {
    var max = 1;
    var min = 1;
    var max_product = Number.MIN_SAFE_INTEGER;

    for (let i = 0; i < nums.length; i++) {
        const value = nums[i];
        var tmp_max = max;

        max = Math.max(value*tmp_max,value*min,value);
        min = Math.min(value*tmp_max,value*min,value);

        // console.log(max + " " + min);

        max_product = Math.max(max,max_product);
    }
    // console.log(max_product);
    return max_product;
};