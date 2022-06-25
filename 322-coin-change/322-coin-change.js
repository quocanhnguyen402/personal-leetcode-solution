/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    result = new Array(amount+1).fill(0);
    for (let i = 0; i < result.length; i++) {

        var min_coin = Number.MAX_SAFE_INTEGER;

        for (let coins_index = 0; coins_index < coins.length; coins_index++) {

            var coin_value = coins[coins_index];

            if( i == coin_value){
                min_coin = 1;
                break;
            } else {
                if( i - coin_value >= 0){
                    if(result[i-coin_value] != -1){
                        min_coin = Math.min(min_coin,result[i-coin_value] + 1);
                    }
                }
            } 
        }

        if(min_coin == Number.MAX_SAFE_INTEGER){
            result[i] = -1;
        } else {
            result[i] = min_coin;
        }
    }

    return amount == 0 ? 0 : result[amount];
};