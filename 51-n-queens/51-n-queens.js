/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function (n) {
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

    function toString(number) {
        var str = "";
        for (let index = 0; index < n; index++) {
            if(index == number){
                str += "Q";
            } else {
                str += ".";
            }
        }
        return str;
    }

    

    helper(0);

    for (let i = 0; i < result.length; i++) {
        for (let j = 0; j < result[i].length; j++) {
            result[i][j] = toString(result[i][j]);
        }
    }

    return result;
};