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

    if (current_target < 0 || index == candidates.length) {
        return;
    }
    
    // Dont add the current value
    var _answer = answer.slice();
    helper(candidates, index + 1, _answer, current_target, result);

    // Add the current value
    _answer.push(candidates[index]);
    helper(candidates, index, _answer, current_target - candidates[index], result);
}