// Given a string and a pattern, find the smallest substring in the given string 
// which has all the characters of the given pattern.

// Input: String="aabdec", Pattern="abc"
// Output: "abdec"
// Explanation: The smallest substring having all characters of the pattern is "abdec"


// Input: String="abdbca", Pattern="abc"
// Output: "bca"
// Explanation: The smallest substring having all characters of the pattern is "bca".

// Input: String="adcad", Pattern="abc"
// Output: ""
// Explanation: No substring in the given string has all characters of the pattern.

const find_substring = function(str, pattern) {
    // TODO: Write your code here
    let windowSeen = {},
        windowStart = 0,
        result = "",
        matched = 0,
        windowEnd = 0;
    for (let i = 0; i < pattern.length; i++) {
        let char = pattern[i]
        windowSeen[char] = (windowSeen[char] || 1) + 1
    }
    while (windowEnd < str.length) {
        let leftChar = str[windowEnd]
        if (windowSeen[leftChar]) {
            if (windowSeen[leftChar] > 1) {
                matched += 1
                windowSeen[leftChar] -= 1
            } else {
                while (windowStart < windowEnd) {
                    let char = str[windowStart]
                    if (windowSeen[char]) {
                        windowSeen[char] += 1
                        matched -= 1
                    }
                    windowStart += 1
                }
                windowEnd -= 1;
            }
        }

        if (matched == pattern.length) {
            c = str.slice(windowStart, windowEnd + 1)
            if (!result || c.length < result) {
                result = c
            }
        };
        windowEnd++
    }

    return result;
}


console.log("Result ", find_substring('aabdec', 'abc'));
console.log("Result ", find_substring('abdbca', 'abc'));
console.log("Result ", find_substring('adcad', 'abc'));