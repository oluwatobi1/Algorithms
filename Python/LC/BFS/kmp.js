// knuth - morris - prath
function getLps(pattern) {
    let arr = Array(pattern.length).fill(0);
    let i = 1;
    let j = 0;
    while (i < pattern.length) {
        if (pattern[i] === pattern[j]) {
            arr[i] = arr[j] + 1;
            i++;
            j++;
        } else {
            if (j == 0) {
                i++
            } else {
                j = 0
            }
        }
    }
    return arr
}

function kmp(haystack, needle) {
    let lps = getLps(needle);
    let i = 0;
    let j = 0;
    let seen = 1;
    while (i < haystack.length) {
        if (haystack[i] == needle[j]) {
            i++;
            j++;
        } else {
            if (j < 1) {
                i++;
            } else {
                j = lps[j - 1]
            }
        }
        console.log("j", j, "needle", needle.length, haystack[i], lps);
        if (j === needle.length) {
            return i - needle.length
        }
    }
    return -1
}

// console.log('kmp ', kmp("aaaab", "aaab"))
// console.log('kmp ', kmp("abcacacab", "cab"))
// console.log('kmp ', kmp("AABAACAABAA", "E"))
console.log('lps ', getLps("aabaaac"))

// knuth-morris-prath algorithm
// https://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
function kmp(haystack, needle) {
    let lps = getLps(needle);
    let i = 0;
    let j = 0;
    while (i < haystack.length) {
        if (haystack[i] == needle[j]) {
            i++;
            j++;
        } else {
            if (j === 0) {
                i++;
            } else {
                j = lps[j - 1]
            }
        }
        if (j === needle.length) {
            return i - needle.length
        }
    }
    return -1
}

function getLps(pattern) {
    let arr = Array(pattern.length).fill(0);
    let i = 1;
    let j = 0;
    while (i < pattern.length) {
        if (pattern[i] === pattern[j]) {
            arr[i] = arr[j] + 1;
            i++;
            j++;
        } else {
            if (j === 0) {
                i++;
            } else {
                j = 0
            }
        }
    }
    return arr
}