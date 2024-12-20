// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
//     You may assume that each input would have exactly one solution, and you may not use the same element twice.
//     You can return the answer in any order.


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const numIndices = {};

    for(let i = 0; i < nums.length; i += 1) {
        const complement = target - nums[i];
        if(numIndices.hasOwnProperty(complement)) {
            return [numIndices[complement], i]
        };
        numIndices[nums[i]] = i;
    }
};