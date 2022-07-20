/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
    var left = 0, right = height.length - 1;
    var max_left = height[left], max_right = height[right];
    var result = 0;
    while(left < right){
        if(max_left <= max_right){
            left++;
            result += calWater(height,left,max_left,max_right);
            max_left = Math.max(max_left,height[left]);
        } else {
            right--;
            result += calWater(height,right,max_left,max_right);
            max_right = Math.max(max_right,height[right]);
        }
    }

    return result;
};

function calWater(height,index,max_left,max_right){
    var water = Math.min(max_left,max_right) - height[index];
    return water > 0 ? water : 0;
}