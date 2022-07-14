var subsets = function (nums) {
    var result = [];
    createSubsets([], 0, nums, result);
    return result;
};

function createSubsets(subset, current_step_length, nums, result) {
    var subset_copy = subset.slice();
    if (current_step_length == nums.length) {
        // Result
        result.push(subset_copy);
    } else {
        // No Add
        createSubsets(subset_copy, current_step_length + 1, nums, result);
        // Add
        subset_copy.push(nums[current_step_length]);
        createSubsets(subset_copy, current_step_length + 1, nums, result);
    }
}