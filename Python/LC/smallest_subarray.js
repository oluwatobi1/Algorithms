const smallest_subarray_with_given_sum = function(s, arr) {
    // TODO: Write your code here
    let windowSum = 0;
    let windowStart = 0;
    let windowEnd = 0;
    let result;

    while (windowStart < arr.length && windowEnd < arr.length) {
        windowSum += arr[windowEnd]
        if (windowSum >= s) {
            curr_result = arr.slice(windowStart, windowEnd + 1)
            if (!result || curr_result.length < result.length) {
                result = curr_result
            }
            windowSum -= arr[windowStart]
            windowSum -= arr[windowEnd]
            windowStart += 1
        } else {
            if (windowEnd < arr.length) {
                windowEnd += 1
            };
        }
    }
    return result;
};
smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])