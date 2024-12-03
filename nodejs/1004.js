/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function(nums, k) {
    let i, j = 0;

    for (i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            k--;
        }
        if (k < 0 && nums[j++] === 0) {
            k++;
        }
    }
};