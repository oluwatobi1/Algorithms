// Cycle in a Circular Array (hard)

// We are given an array containing positive and negative numbers. Suppose the array 
// contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move 
// forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume 
// that the array is circular which means two things:

//     If, while moving forward, we reach the end of the array, we will jump to the first 
//     element to continue the movement.
//     If, while moving backward, we reach the beginning of the array, we will jump to the 
//     last element to continue the movement.

// Write a method to determine if the array has a cycle. The cycle should have more than one 
// element and should follow one direction which means the cycle should not contain both forward 
// and backward movements.

// Example 1:

// Input: [1, 2, -1, 2, 2]
// Output: true
// Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0

// Example 2:

// Input: [2, 2, -1, 2]
// Output: true
// Explanation: The array has a cycle among indices: 1 -> 3 -> 1

// Example 3:

// Input: [2, 1, -1, -2]
// Output: false
// Explanation: The array does not have any cycle.

const circular_array_loop_exists = function(arr) {
    // TODO: Write your code here
    for (let i = 0; i < arr.length; i++) {
        let isForward = arr[i] >= 0;
        let fast = i,
            slow = i;
        while (true) {
            slow = find_next_index(arr, isForward, slow);
            console.log('slow', slow)
            fast = find_next_index(arr, isForward, fast);

            if (fast !== -1) {
                fast = find_next_index(arr, isForward, fast);
            };
            if (slow === -1 || fast === -1 || slow === fast) {
                break;
            };
        }
        if (slow !== -1 && slow === fast) {
            return true
        }
    }
    return false;
};

const find_next_index = function(arr, isForward, currentIndex) {
    let direction = arr[currentIndex] >= 0;
    if (direction !== isForward) return -1;

    let nextIndex = (currentIndex + arr[currentIndex]) % arr.length
    if (nextIndex < 0) {
        nextIndex = nextIndex + arr.length;
    };
    if (nextIndex === currentIndex) {
        nextIndex = -1
    }
    return nextIndex
}


console.log(`${circular_array_loop_exists([1, 2, -1, 2, 2])}`)
console.log(`${circular_array_loop_exists([2, 2, -1, 2])}`)
console.log(`${circular_array_loop_exists([2, 1, -1, -2])}`)