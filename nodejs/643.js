/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let maxSum = 0
    let currentSum = 0

    for(let i = 0; i < k; i++){
        currentSum += nums[i]
    }

    maxSum = currentSum

    for(let i = k; i < nums.length; i++){
        currentSum += nums[i] - nums[i - k]
        if(currentSum > maxSum){
            maxSum = currentSum
        }
    }

    return maxSum / k

};