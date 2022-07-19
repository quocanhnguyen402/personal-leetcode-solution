/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {

    if(digits == ""){
        return [];
    }

    var result = [];

    function helper(i, current_string) {
        if (i >= digits.length) {
            result.push(current_string)
            return;
        }

        for (let j = 0; j < phones[digits[i]].length; j++) {
            current_string += phones[digits[i]][j];
            helper(i + 1, current_string);
            current_string = current_string.slice(0, -1);
        }
    }

    var phones = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }

    helper(0, "", phones);

    return result;
};