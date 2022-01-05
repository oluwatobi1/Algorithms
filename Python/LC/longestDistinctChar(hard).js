// Sliding Window
// Given a string, find the length of the longest substring, which has all distinct characters.

// Input: String="aabccbb"
// Output: 3
// Explanation: The longest substring with distinct characters is "abc".

// Input: String="abbbb"
// Output: 2
// Explanation: The longest substring with distinct characters is "ab".

// Input: String="abccde"
// Output: 3
// Explanation: Longest substrings with distinct characters are "abc" & "cde".


const non_repeat_substring = function(str) {
    // TODO: Write your code here
    let result = 0,
        cache,
        windowSeen = {},
        windowStart = 0,
        windowEnd = 0;

    while (windowEnd < str.length) {
        let rightChar = str[windowEnd]
        windowSeen[rightChar] = (windowSeen[rightChar] || 0) + 1;

        if (windowSeen[rightChar] < 2) {
            let uniqueStreak = windowEnd - windowStart + 1;
            cache = str.slice(windowStart, windowEnd + 1)
            console.log(cache, uniqueStreak);
            if (uniqueStreak > result) {
                result = uniqueStreak
            };
        } else {
            windowStart = windowEnd
        };

        windowEnd += 1
    };
    return result
};


console.log(`Length of the longest substring: ${non_repeat_substring('aabccbb')}`);
console.log(`Length of the longest substring: ${non_repeat_substring('abbbb')}`);
console.log(`Length of the longest substring: ${non_repeat_substring('abccde')}`);