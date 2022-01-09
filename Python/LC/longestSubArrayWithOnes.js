const length_of_longest_substring = function(arr, k) {
    // TODO: Write your code here
    let windowEnd = 0,
        windowSeen = {},
        result = 0,
        windowStart = 0,
        zeros = 0,
        ones = 1;
    console.log("Start");
    while (windowEnd < arr.length) {
        if (windowSeen[zeros] > k && windowSeen[ones] > k) {
            console.log("if cond", arr.slice(windowStart, windowEnd));
            console.log('windowSeen', windowSeen, 'result', result);
            let size = windowEnd - windowStart - 1;
            if (result < size) {
                result = size
            };
            windowSeen[arr[windowStart]] -= 1
            windowStart += 1
            console.log("2 windowSeen", windowSeen, 'result', result, "size", size);
        } else {
            rightEl = arr[windowEnd]
            windowSeen[rightEl] = (windowSeen[rightEl] || 0) + 1
            console.log("loop, windowSeen", windowSeen);
            windowEnd += 1
        }
    }
    let size = windowEnd - windowStart;
    console.log("end size", size);
    if (result < size) {
        result = size
    };
    return result
};


console.log(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2));
console.log(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3));