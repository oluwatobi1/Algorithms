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

        while (matched == pattern.length) {
            let char = str[windowStart]
            c = str.slice(windowStart, windowEnd + 1)
            if (!result || c.length < result) {
                result = c
            }
            if (windowSeen[char]) {
                matched -= 1
            }
            windowStart += 1
        };
        windowEnd++
    }

    return result;
}

// function find_substring(str, pattern) {
//     let windowStart = 0,
//         matched = 0,
//         substrStart = 0,
//         minLength = str.length + 1,
//         charFrequency = {};

//     for (i = 0; i < pattern.length; i++) {
//         const chr = pattern[i];
//         if (!(chr in charFrequency)) {
//             charFrequency[chr] = 0;
//         }
//         charFrequency[chr] += 1;
//     }

//     // try to extend the range [windowStart, windowEnd]
//     for (windowEnd = 0; windowEnd < str.length; windowEnd++) {
//         const rightChar = str[windowEnd];
//         if (rightChar in charFrequency) {
//             charFrequency[rightChar] -= 1;
//             if (charFrequency[rightChar] >= 0) { // Count every matching of a character
//                 matched += 1;
//             }
//         }

//         // Shrink the window if we can, finish as soon as we remove a matched character
//         while (matched === pattern.length) {
//             if (minLength > windowEnd - windowStart + 1) {
//                 minLength = windowEnd - windowStart + 1;
//                 substrStart = windowStart;
//             }

//             const leftChar = str[windowStart];
//             windowStart += 1;
//             if (leftChar in charFrequency) {
//                 // Note that we could have redundant matching characters, therefore we'll decrement the
//                 // matched count only when a useful occurrence of a matched character is going out of the window
//                 if (charFrequency[leftChar] === 0) {
//                     matched -= 1;
//                 }
//                 charFrequency[leftChar] += 1;
//             }
//         }
//     }

//     if (minLength > str.length) {
//         return '';
//     }
//     return str.substring(substrStart, substrStart + minLength);
// }



console.log("Result ", find_substring('aabdec', 'abc'));
console.log("Result ", find_substring('abdbca', 'abc'));
console.log("Result ", find_substring('adcad', 'abc'));
console.log("Result ", find_substring('absibdibsibwbs', 'bdb'));