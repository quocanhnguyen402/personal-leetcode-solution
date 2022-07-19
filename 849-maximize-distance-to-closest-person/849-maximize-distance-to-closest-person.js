/**
 * @param {number[]} seats
 * @return {number}
 */
var maxDistToClosest = function(seats) {
    var max_dist = Number.MIN_SAFE_INTEGER;
    var result_seat = 0;

    for (let i = 0; i < seats.length; i++) {
        if( seats[i] == 1){
            continue;
        } else {
            var left_dist = 0;
            var left_pointer = i;
            var right_dist = 0;
            var right_pointer = i;
            
            if(i == seats.length-1){
                right_dist = Number.MAX_SAFE_INTEGER;
            }

            if(i == 0){
                left_dist = Number.MAX_SAFE_INTEGER;
            }

            while(left_pointer >= 0 && seats[left_pointer] == 0){
                left_pointer--;
                left_dist++;
            }

            while(right_pointer <= seats.length && seats[right_pointer] == 0){
                right_pointer++;
                right_dist++;
            }

            var dist = Math.min(left_dist,right_dist);

            if(dist > max_dist){
                max_dist = dist;
                result_seat = i;
            }
        }
    }

    return max_dist;
}