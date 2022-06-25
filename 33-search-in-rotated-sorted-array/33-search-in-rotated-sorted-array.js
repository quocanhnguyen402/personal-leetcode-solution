/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    var left = 0;
    var right = nums.length-1;
    
    while (left <= right) {
        var mid = Math.floor((right+left)/2);

        if(target == nums[mid]){
            return mid;
        }

        if(nums[left] <= nums[mid]){
            if(target < nums[mid] && target >= nums[left]){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            if(target > nums[mid] && target <= nums[right]){
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }

    return -1;
};