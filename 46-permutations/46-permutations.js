/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function (nums) {
    var result = [];
    helper(nums, new Set(), 0 ,result);
    return result;
};

function helper(nums, permute, pos,result) {
    if (pos >= nums.length) {
        result.push(Array.from(permute));
        return;
    }

    if(permute.size >= pos + 1 ){
        return;
    }

    var clone = new Set(permute);
    for (let index = 0; index < nums.length; index++) {
        const element = nums[index];
        if (clone.has(element)) {
            continue
        }
        clone.add(element);
        helper(nums, clone, pos + 1,result);
        clone.delete(element);
    }

}