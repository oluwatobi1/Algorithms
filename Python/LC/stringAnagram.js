// Given a string and a pattern, find all anagrams of the pattern in the given string.

// Input: String="ppqp", Pattern="pq"
// Output: [1, 2]
// Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

// Input: String="abbcabc", Pattern="abc"
// Output: [2, 3, 4]
// Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

const find_string_anagrams = function(str, pattern) {
    let result_indexes = [],
        windowStart = 0,
        matched = 0,
        windowSeen = {};

    for (i = 0; i < pattern.length; i++) {
        let rightChar = pattern[i]
        windowSeen[rightChar] = (windowSeen[rightChar] || 0) + 1
    }
    // TODO: Write your code here

    for (i = 0; i < str.length; i++) {
        let currChar = str[i]
        if (i > pattern.length - 1) {
            let leftChar = str[windowStart];
            if (leftChar in windowSeen) {
                windowSeen[leftChar] += 1
                if (windowSeen[leftChar] > 0) {
                    matched -= 1
                }
            }
            windowStart += 1
        }
        if (currChar in windowSeen) {
            windowSeen[currChar] -= 1
            if (windowSeen[currChar] > -1) {
                matched += 1
            }
        }
        if (matched === pattern.length) {
            result_indexes.push(i - matched + 1)
        }
    }
    return result_indexes;
};

console.log("Output ", find_string_anagrams("ppqp", 'pq'));
console.log("Output ", find_string_anagrams("abbcabc", 'abc'));
console.log("Output ", find_string_anagrams("aaaaaaaaa", 'a'));