/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    const length = matrix.length;
    var left = 0;
    var right = length - 1;
    var temp = 0;
    while (left < right) {
        var top = left;
        var bottom = right;
        for (let i = 0; i <= right-left - 1; i++) {
            temp = matrix[top][left + i];
            matrix[top][left + i] = matrix[bottom - i][left];
            matrix[bottom - i][left] = matrix[bottom][right - i];
            matrix[bottom][right - i] = matrix[top + i][right];
            matrix[top + i][right] = temp;
        }
        left = left + 1;
        right = right - 1;
    }
};