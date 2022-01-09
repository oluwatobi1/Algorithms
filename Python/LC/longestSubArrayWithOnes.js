const length_of_longest_substring = function(arr, k) {
    // TODO: Write your code here
    // Second solution
    let result = 0,
        windowStart = 0,
        maxLength = 0,
        maxOnes = 0;
    for (windowEnd = 0; windowEnd < arr.length; windowEnd++) {
        if (arr[windowEnd] === 1) {
            maxOnes += 1
        };
        if (windowEnd - windowStart + 1 - maxOnes > k) {
            if (arr[windowStart] === 1) {
                maxOnes -= 1
            }
            windowStart += 1
        }
        maxLength = Math.max(maxLength, windowEnd - windowStart + 1)
    }
    return maxLength
}


console.log(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2));
console.log(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3));