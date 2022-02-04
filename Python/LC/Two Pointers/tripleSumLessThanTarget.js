// Given an array arr of unsorted numbers and a target sum, count all triplets
//  in it such that arr[i] + arr[j] + arr[k] < target where i, j, and 
// k are three different indices. Write a function to return the count of such triplets.


// Input: [-1, 0, 2, 3], target=3 
// Output: 2
// Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]


const triplet_with_smaller_sum = function(arr, target) {
    count = 0;
    // TODO: Write your code here
    arr.sort((a, b) => a - b)
    for (let i = 0; i < arr.length; i++) {
        if (i > 0 && arr[i] == arr[i - 1]) continue;
        count = search_triple_pair(arr, i + 1, i, count, target)
    }
    return count;
};

const search_triple_pair = function(arr, left, currItem, count, target) {
    let right = arr.length - 1;
    while (left < right) {
        let currSum = arr[currItem] + arr[left] + arr[right]
        if (currSum < target) {
            count += right - left;
            left += 1;
        } else {
            right -= 1;
        };
    };
    return count
}


console.log("Result", triplet_with_smaller_sum([-1, 2, 0, 3], 3));
console.log("Result", triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5));