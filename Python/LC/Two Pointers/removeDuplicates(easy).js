// Given an array of sorted numbers, remove all duplicates from it.
//  You should not use any extra space; after removing the duplicates in-place
//  return the length of the subarray that has no duplicate in it.

// Input: [2, 3, 3, 3, 6, 9, 9]
// Output: 4
// Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

// Input: [2, 2, 2, 11]
// Output: 2
// Explanation: The first two elements after removing the duplicates will be [2, 11].


const remove_duplicates = function(arr) {
    // TODO: Write your code here
    if (arr.length < 2) {
        return arr.length
    };

    let startPointer = 0,
        nextPointer = 1
    count = 1;
    while (nextPointer < arr.length) {
        // console.log("arr", arr.slice(0, nextPointer + 1));
        if (arr[startPointer] === arr[nextPointer]) {
            // console.log("point", arr[startPointer], arr[nextPointer]);
            nextPointer += 1

        } else {
            // console.log("Not equal", arr[nextPointer], arr[startPointer]);
            count += 1
            startPointer = nextPointer
            nextPointer += 1;
        }
        // console.log("pointer", startPointer, nextPointer);
    }
    return count;
};


console.log(remove_duplicates([2, 3, 3, 3, 6, 9, 9]));
console.log(remove_duplicates([2, 2, 2, 2, 3]));
console.log(remove_duplicates([6]));