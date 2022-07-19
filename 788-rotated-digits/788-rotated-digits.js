/**
 * @param {number} n
 * @return {number}
 */
 var rotatedDigits = function(n) {
    var result = [];
    for (let i = 1; i <= n; i++) {
        if(check(i)){
            result.push(i);
        }
    }
    return result.length;
};
 
function check(int){
    var origin_int = int;
    var transform = [0,1,5,-1,-1,2,9,-1,8,6];
    
    if(transform[int % 10] == -1 ){
        return false;
    }
    
    var new_int = transform[int % 10];
    int = Math.floor(int/10);
    var index = 1;

    while(int > 0){
        if(transform[int % 10] == -1 ){
            return false;
        }
        new_int = transform[int % 10]*Math.pow(10,index) + new_int;
        int = Math.floor(int/10);
        index++;
    }

    if(origin_int != new_int){
        return true;
    } else {
        return false
    }
}