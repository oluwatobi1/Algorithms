// Given a string and a pattern, find all anagrams of the pattern in the given string.
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
    console.log(" Start windowSeen", windowSeen);

    for (i = 0; i < str.length; i++) {
        let currChar = str[i]
        if (i > pattern.length - 1) {
            let leftChar = str[windowStart];
            console.log("leftchar", leftChar, windowSeen);
            if (leftChar in windowSeen) {
                windowSeen[leftChar] += 1
                if (windowSeen[leftChar] > 0) {
                    matched -= 1
                }
                console.log('////windo', windowSeen, "matched", matched);
            }
            windowStart += 1
        }
        console.log("firest window", windowSeen, "currChar", currChar, "i", i);
        if (currChar in windowSeen) {
            windowSeen[currChar] -= 1
            if (windowSeen[currChar] > -1) {
                matched += 1
            }
            console.log("matched", matched);
        }
        if (matched === pattern.length) {
            result_indexes.push(i - matched + 1)
            console.log("matched", matched, "pattern", pattern.length, "i", i, 'str', str, 'result', result_indexes);
        }


        console.log("..Window Seen ", windowSeen,
            'window', str.slice(windowStart, i), "matched", matched);
    }
    return result_indexes;
};

console.log("Output ", find_string_anagrams("ppqp", 'pq'));
console.log("Output ", find_string_anagrams("abbcabc", 'abc'));