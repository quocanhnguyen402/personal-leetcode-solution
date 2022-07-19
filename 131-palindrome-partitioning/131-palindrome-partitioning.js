/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function (s) {
    var result = [];
    var part = [];

    search_dfs(0, s, part);

    function search_dfs(i) {
        if (i >= s.length) {
            result.push(part.slice());
            return;
        }
    
        for (let j = i; j < s.length; j++) {
            var substring = s.slice(i, j + 1);
            if (checkPalindrome(substring)) {
                part.push(substring);
                search_dfs(j + 1);
                part.pop();
            }
        }
    }
    
    function checkPalindrome(s) {
        var left = 0;
        var right = s.length - 1;
        while (left <= right) {
            if (s[left] != s[right]) {
                return false;
            } else {
                left++;
                right--;
            }
        }
        return true
    }

    return result;
};