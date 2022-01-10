const find_permutation = function(str, pattern) {
    // TODO: Write your code here
    let windowStart = 0,
        windowEnd = 0;
    console.log("Starting ......", str);
    while (windowEnd < str.length) {
        rightChar = str[windowEnd]
        console.log("current char", rightChar);
        if (rightChar === pattern[0]) {
            // console.log("found ", rightChar);
            // open window
            let left = Math.max(windowStart, windowEnd - pattern.length)
            let right = Math.min(str.length, windowEnd + pattern.length)
                // check for permutation
            let permInString = str.substr(left, right)
            console.log('permString', permInString, ':::::pattern', pattern, "left", left, 'right', right);
            let permCheck = pattern
            for (i = 0; i < permInString.length; i++) {
                console.log("permcheck", permCheck);
                if (permCheck.includes(permInString[i])) {
                    permCheck = permCheck.replace(permInString[i], '')
                } else {
                    permCheck = pattern
                };
                if (permCheck.length < 1) {
                    return true
                }
            };
            console.log("done Perm Check", "left", left, 'right', right);
            // shift both windowStart and windowEnd
            windowStart = right - 1;
            windowEnd = right - 1
            windowEnd -= 1
            console.log("window start", windowStart, "WIndow end", windowEnd, 'str end', str.slice(windowEnd, ));
        }
        windowEnd += 1
    }
    return false;
};

console.log(find_permutation('oidbcaf', 'abc'));
console.log(find_permutation('bcdxabcdy', 'bcdyabcdx'));
console.log(find_permutation('aaacb', 'abc'));
console.log(find_permutation('odicf', 'dc'));
console.log(find_permutation('dcabcde', 'decb'));