// Given an array with positive numbers and a positive target number, 
// find all of its contiguous subarrays whose product is less than the target number.

// Input: [2, 5, 3, 10], target=30 
// Output: [2], [5], [2, 5], [3], [5, 3], [10]
// Explanation: There are six contiguous subarrays whose product is less than the target.

// Input: [8, 2, 6, 5], target=50 
// Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
// Explanation: There are seven contiguous subarrays whose product is less than the target.


// const Deque = require('./collections/deque'); //http://www.collectionsjs.com


function find_subarrays(arr, target) {
    let result = [],
        product = 1,
        left = 0;
    for (right = 0; right < arr.length; right++) {
        product *= arr[right];
        while ((product >= target && left < arr.length)) {
            product /= arr[left];
            left += 1;
        }
        // since the product of all numbers from left to right is less than the target therefore,
        // all subarrays from left to right will have a product less than the target too; to avoid
        // duplicates, we will start with a subarray containing only arr[right] and then extend it
        const tempList = new Array();
        for (let i = right; i > left - 1; i--) {
            tempList.unshift(arr[i]);
            result.push(tempList);
        }
    }
    return result;
}


const find_sub = function(arr, target) {
    console.log("start; \narr", arr);
    let result = [],
        product = 1,
        left = 0;

    for (let right = 0; right < arr.length; right++) {
        product *= arr[right]
        console.log("product", product);
        while ((product >= target && left < arr.length)) {
            product /= arr[left]
            left += 1
            console.log("above targ", product, "target", target);
        }

        const tempList = new Array();
        for (let i = right; i > left - 1; i--) {
            tempList.unshift(arr[i])
            result.push(tempList)

            console.log("right & left", right, left);
            console.log("tempList", tempList, "result", result);
        };



    }
}

console.log(find_sub([2, 5, 3, 10], 33));
console.log(find_sub([8, 2, 6, 5], 50));