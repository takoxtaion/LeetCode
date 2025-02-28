/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    nums.sort((a,b) => (Number(String(b)+String(a)))-(Number(String(a)+String(b))))
    let result = nums.join("")
    if(nums[0] == 0){
        return "0"
    }else{
        return result
    }
};