/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
    var result = [];
    nums = nums.sort((a, b) => { return a - b });
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > 0) {
            return result;
        }
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }
        var twoSum = _twoSum(nums, i + 1, nums.length - 1, 0 - nums[i]);
        for (let index = 0; index < twoSum.length; index++) {
            twoSum[index].push(nums[i]);
            result.push(twoSum[index]);
        }
    }
    return result;
};

function _twoSum(numbers, left, right, target) {
    var result_sum = [];
    while (left < right) {
        var sum = numbers[left] + numbers[right];
        if (sum == target) {
            result_sum.push([numbers[left], numbers[right]]);
            left++;
            right--;
            while (numbers[left] == numbers[left - 1]) {
                left++
            };
            while (numbers[right] == numbers[right + 1]) {
                right--
            };
        } else if (sum > target) {
            right--;
        } else {
            left++;
        }
    }
    return result_sum;
};