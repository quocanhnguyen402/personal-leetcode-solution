/**
 * @param {number[]} nums
 * @return {number[][]}
 */
 var subsetsWithDup = function (nums) {
    var result = [];
    nums.sort();
    createSubsets([], 0, nums, result);
    return result;
};

function createSubsets(subset, cur_index, nums, result) {
    
    var subset_copy = subset.slice();
    console.log(subset_copy)
    if (cur_index > nums.length) {
        return;
    }

    if (cur_index == nums.length) {
        // Result
        result.push(subset_copy);
    } else {
        
        // Include the element
        subset_copy.push(nums[cur_index]);
        createSubsets(subset_copy, cur_index + 1, nums, result);
        subset_copy.pop();

        // Dont include the element if there is dupes
        while(cur_index < nums.length - 1 && nums[cur_index] == nums[cur_index+1]){
            cur_index++;
        }
        createSubsets(subset_copy, cur_index + 1, nums, result);
    }
}