// Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    if(num <= 9) {
        return num;
    };
    return 1 + (num - 1) % 9;
};