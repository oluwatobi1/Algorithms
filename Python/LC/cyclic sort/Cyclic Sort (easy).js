// We are given an array containing n objects. Each object, when created, was assigned a 
// unique number from the range 1 to n based on their creation sequence.
//  This means that the object with sequence number 3 was created just before the object with 
//  sequence number 4.

// Write a function to sort the objects in-place on their creation sequence number in O(n)
// O(n)
//  and without using any extra space. For simplicity, let’s assume we are passed an integer
//   array containing only the sequence numbers, though each number is actually an object.

// Example 1:

// Input: [3, 1, 5, 4, 2]
// Output: [1, 2, 3, 4, 5]
// Example 2:

// Input: [2, 6, 4, 3, 1, 5]
// Output: [1, 2, 3, 4, 5, 6]
// Example 3:

// Input: [1, 5, 6, 4, 3, 2]
// Output: [1, 2, 3, 4, 5, 6]


const cyclic_sort = function(nums) {
    // TODO: Write your code here
    let i = 0;
    while (i < nums.length) {
        const supposedIndex = nums[i] - 1;
        if (nums[i] != nums[supposedIndex]) {
            [nums[i], nums[supposedIndex]] = [nums[supposedIndex], nums[i]];
        } else {
            i++;
        }
    }
}


console.log(`${cyclic_sort([3, 1, 5, 4, 2])}`)
console.log(`${cyclic_sort([2, 6, 4, 3, 1, 5])}`)
console.log(`${cyclic_sort([1, 5, 6, 4, 3, 2])}`)