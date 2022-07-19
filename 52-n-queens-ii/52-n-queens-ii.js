/**
 * @param {number} n
 * @return {string[][]}
 */
var totalNQueens = function (n) {
    var result = [];
    var placement = [];
    function helper(row) {

        if (row >= n) {
            result.push(placement.slice());
            return;
        }

        for (let i = 0; i < n; i++) {
            var test = test_queen(row, i, placement);
            if (test) {
                placement.push(i);
                helper(row + 1);
                placement.pop();
            }

        }
    }

    function test_queen(row, queen_position, placement) {
        for (let i = 0; i < placement.length; i++) {
            if (queen_position == placement[i]) {
                return false;
            }

            if (queen_position == placement[i] + (row - i) || queen_position == placement[i] - (row - i)) {
                return false;
            }

        }

        return true;
    }

    helper(0);

    return result.length;
};