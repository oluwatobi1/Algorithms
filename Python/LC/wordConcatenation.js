// Input: String="catfoxcat", Words=["cat", "fox"]
// Output: [0, 3]
// Explanation: The two substring containing both the words are "catfox" & "foxcat".

// Input: String="catcatfoxfox", Words=["cat", "fox"]
// Output: [3]
// Explanation: The only substring containing both the words is "catfox".


const find_word_concatenation = function(str, words) {
    result_indices = [];
    // TODO: Write your code here
    // get length of entire words
    let wordStrings = words.join(""),
        windowStart = 0;

    // create window of lenght and temp word array
    // iter through temp word array and remove from each word from temp if found
    // when temp is empty append start index to result

    for (let windowEnd = wordStrings.length; windowEnd <= str.length; windowEnd++) {
        let temp = [...words]
        let currString = str.slice(windowStart, windowEnd)
        for (let i = 0; i < words.length; i++) {
            let itemIndex = currString.indexOf(words[i])
            if (itemIndex !== -1) {
                temp.splice(temp.indexOf(i), 1)
            }
            if (temp.length == 0) {
                result_indices.push(windowStart)
            }
        }
        windowStart += 1
    }
    return result_indices;
};

console.log("RESULT ", find_word_concatenation("catfoxcat", ["cat", "fox"]))
console.log("RESULT ", find_word_concatenation("catcatfoxfox", ["cat", "fox"]))
console.log("RESULT ", find_word_concatenation("catcatfoxsheepfox", ["cat", "fox", "sheep"]))