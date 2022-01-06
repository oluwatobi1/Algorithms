const length_of_longest_substring = function(str, k) {
    // TODO: Write your code here
    let windowStart = 0,
        windowEnd = 0,
        windowSeen = {},
        result = 0;

    while (windowEnd < str.length) {
        let rightChar = str[windowEnd]
        windowSeen[rightChar] = (windowSeen[rightChar] || 0) + 1
        console.log('String', str.slice(windowEnd, ));
        console.log('Full String', str);
        if (Object.keys(windowSeen).length > 1) {
            console.log("starting");
            if (Object.keys(windowSeen).length == 2) {
                var pause = windowStart;
                windowStart = windowEnd;
                var point = windowEnd - 1;
                windowEnd -= 1
                console.log("now ", pause, windowStart, 'point', point, temp, str, str[windowEnd]);

            }
            console.log("windowSeen", windowSeen);
            var temp = {},
                c = 0;
            // console.log("temp", temp);
            temp[str[point]] = windowEnd + 1 - pause
            console.log("tempin", temp, windowStart, "windowEnd", windowEnd, 'pause', pause, 'windowStart', windowStart);
            for (let i = point; i < str.length; i++) {
                console.log("for loop", str.slice(i, ), "c", c, 'temp', temp);
                if (c < k) {
                    temp[str[point]] += 1
                    c += 1
                } else {
                    temp[str[i]] = (temp[str[i]] || 0) + 1;
                    if (Object.keys(temp).length > 1) {
                        console.log("wmnd", temp);
                        if (temp[str[point]] > result) {
                            result = temp[str[point]]
                            console.log("result update", temp, temp[str[point]], result, str[windowEnd]);
                            temp = {}
                        }
                        break
                    }
                    break
                }
                // console.log("Setemp", temp);
            }
            windowSeen = {}
        };
        windowEnd += 1
    };

    return result;
};



console.log("....Length_of_longest_substring", length_of_longest_substring('aabcdbb', 2));
console.log("....length_of_longest_substring", length_of_longest_substring('abbcb', 1));
console.log("....length_of_longest_substring", length_of_longest_substring('abccde', 1));