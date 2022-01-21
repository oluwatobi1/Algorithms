// Input: String="catfoxcat", Words=["cat", "fox"]
// Output: [0, 3]
// Explanation: The two substring containing both the words are "catfox" & "foxcat".

// Input: String="catcatfoxfox", Words=["cat", "fox"]
// Output: [3]
// Explanation: The only substring containing both the words is "catfox".


const find_word_concatenation = function(str, words) {
    result_indices = [];
    // TODO: Write your code here
    return result_indices;
};

console.log("RESULT ", find_word_concatenation("catfoxcat", ["cat", "fox"]))
console.log("RESULT ", find_word_concatenation("catcatfoxfox", ["cat", "fox"]))