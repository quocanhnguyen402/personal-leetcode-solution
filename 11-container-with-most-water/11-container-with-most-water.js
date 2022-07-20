/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
    var left = 0, right = height.length - 1;
    var max_area = area(left, right, height);
    while (left < right) {
        if (height[left] <= height[right]) {
            left++;
        } else {
            right--;
        }
        max_area = Math.max(max_area,area(left,right,height));
    }
    return max_area;
};

function area(left, right, height) {
    return (right - left) * Math.min(height[left], height[right]);
}