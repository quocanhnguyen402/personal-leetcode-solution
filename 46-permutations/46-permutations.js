/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function (nums) {
    var result = [];
    helper(nums, new Set() ,result);
    return result;
};

function helper(nums, permute,result) {
    if (permute.size == nums.length) {
        result.push(Array.from(permute));
        return;
    }

    var clone = new Set(permute);
    for (let index = 0; index < nums.length; index++) {
        const element = nums[index];
        if (clone.has(element)) {
            continue
        }
        clone.add(element);
        helper(nums, clone,result);
        clone.delete(element);
    }

}