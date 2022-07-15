/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
    var result = [];
    helper(candidates, 0, [], target, result);
    return result;
};

function helper(candidates, index, answer, current_target, result) {

    if (current_target == 0) {
        result.push(answer.slice());
        return;
    }

    if (current_target < 0) {
        return;
    }

    if (index == candidates.length) {
        return;
    }

    var current_value = candidates[index];

    // Dont add the current value
    var _answer_no = answer.slice();
    helper(candidates, index + 1, _answer_no, current_target, result);

    // Add the current value
    var _answer = answer.slice();
    _answer.push(current_value);
    helper(candidates, index, _answer, current_target - current_value, result);
}