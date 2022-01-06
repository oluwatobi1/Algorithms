const length_of_longest_substring = function(str, k) {
    // TODO: Write your code here
    let windowStart = 0,
        windowEnd = 0,
        windowSeen = {},
        result = 0;

    while (windowEnd < str.length) {
        let rightChar = str[windowEnd];
        windowSeen[rightChar] = (windowSeen[rightChar] || 0) + 1

        if (Object.keys(windowSeen).length > 1) {
            windowEnd -= 1
            let temp = {},
                c = 0;;
            temp[str[windowEnd]] = windowSeen[str[windowEnd]];
            for (let i = windowEnd + 1; i < str.length; i++) {
                if (c < k) {
                    temp[str[windowEnd]] += 1;
                    c += 1
                } else {
                    temp[str[i]] = (temp[str[i]] || 0) + 1;
                    previousChar = temp[str[windowEnd]]
                    if (previousChar > result) {
                        result = previousChar;
                    };
                    if (Object.keys(temp).length > 1) {
                        temp = {};
                        break;
                    };
                }
            }
            windowSeen = {}
        };
        windowEnd += 1
    }

    return result;
};



console.log("....Length_of_longest_substring", length_of_longest_substring('aabcdbb', 2));
console.log("....Length_of_longest_substring", length_of_longest_substring('abbcb', 1));
console.log("....Length_of_longest_substring", length_of_longest_substring('abccde', 1));