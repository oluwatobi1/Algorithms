// Given an array with positive numbers and a positive target number, 
// find all of its contiguous subarrays whose product is less than the target number.

// Input: [2, 5, 3, 10], target=30 
// Output: [2], [5], [2, 5], [3], [5, 3], [10]
// Explanation: There are six contiguous subarrays whose product is less than the target.

// Input: [8, 2, 6, 5], target=50 
// Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
// Explanation: There are seven contiguous subarrays whose product is less than the target.


const find_subarrays = function(arr, target) {
    let result = [],
        left = 0
    product = 1;

    for (let right = 0; right < arr.length; right++) {
        product *= arr[right]
        while (product > target && left <= right) {
            product /= arr[left];
            left += 1;
        }
        let tempList = []
        for (let i = left; i < right + 1; i++) {
            tempList.push(arr[i])
            result.push(tempList)
        }
    }
    return result
};

console.log("result", find_subarrays([2, 3, 5, 2, 6, 4], 30))