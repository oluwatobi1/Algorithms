// Given a string, find the length of the longest substring in it with no more than K distinct characters.

// Input: String="araaci", K=2
// Output: 4
// Explanation: The longest substring with no more than '2' distinct characters is "araa".

// Input: String="cbbebi", K=3
// Output: 5
// Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

// Input: String="cbbebi", K=10
// Output: 6
// Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".

const longest_substring_with_k_distinct = function(str, k) {
    // TODO: Write your code here
    let windowSeen = new Set(),
        windowStart = 0,
        result = 0,
        windowEnd = 0;

    while (windowEnd < str.length) {
        windowSeen.add(str[windowEnd])
        console.log(str.slice(windowStart, windowEnd));
        if (windowSeen.size > k) {
            curr_length = windowEnd - windowStart
            if (curr_length > result) {
                result = curr_length
            };
            windowSeen.delete(str[windowStart]);
            windowStart += 1
        };
        windowEnd += 1
    };
    return result;
};

longest_substring_with_k_distinct("araaci", 1)
longest_substring_with_k_distinct("cbbebi", 10)