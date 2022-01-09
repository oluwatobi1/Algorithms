const length_of_longest_substring = function(arr, k) {
    // TODO: Write your code here
    // This solution is for exchanging either zero with one or 
    // one with zeros (dynamic)
    let windowEnd = 0,
        windowSeen = {},
        result = 0,
        windowStart = 0,
        zeros = 0,
        ones = 1;
    while (windowEnd < arr.length) {
        if (windowSeen[zeros] > k && windowSeen[ones] > k) {
            let size = windowEnd - windowStart - 1;
            if (result < size) {
                result = size
            };
            windowSeen[arr[windowStart]] -= 1
            windowStart += 1
        } else {
            rightEl = arr[windowEnd]
            windowSeen[rightEl] = (windowSeen[rightEl] || 0) + 1
            windowEnd += 1
        }
    }
    let size = windowEnd - windowStart;
    if (result < size) {
        result = size
    };
    return result
};


console.log(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2));
console.log(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3));