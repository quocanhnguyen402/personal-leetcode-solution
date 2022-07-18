/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function (candidates, target) {
    var result = [];
    helper(candidates.sort(), 0, [], target, result);
    return result;
};

function helper(candidates, index, answer, current_target, result) {

    if (current_target == 0) {
        result.push(answer.slice());
        return;
    }

    if (current_target < 0 || index == candidates.length) {
        return;
    }

    var _answer = answer.slice();

    // Use the current value
    _answer.push(candidates[index]);
    helper(candidates, index + 1, _answer, current_target - candidates[index], result);
    _answer.pop()

    // Don't use the current value anymore
    while (index < candidates.length - 1 && candidates[index] == candidates[index + 1]) {
        index++;
    }
    helper(candidates, index + 1, _answer, current_target, result);
}