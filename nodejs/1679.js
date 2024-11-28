/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    nums.sort((a, b) => a - b)
    let count = 0
    let i = 0, j = nums.length - 1
    while(i < j){
        let aux = nums[i] + nums[j]
        if(aux === k){
            i++
            j--
            count++
        } else if(aux > k) {
            j--
        } else{
            i++
        }
    }
    return count
};