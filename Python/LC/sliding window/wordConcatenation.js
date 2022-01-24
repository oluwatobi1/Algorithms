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



// const find_word_concatenation = function(str, words) {
//     if (words.length === 0 || words[0].length === 0) {
//         return []
//     }
//     // initialize hash map
//     let wordFrequency = {};
//     const result = [];
//     // add all item in word to hash map
//     words.forEach((word) => {
//         wordFrequency[word] = (wordFrequency[word] || 0) + 1
//     })
//     // initialize wordsCount and wordLength
//     let wordsCount = words.length,
//     wordLen

// };


// function find_word_concatenation(str, words) {
//     if (words.length === 0 || words[0].length === 0) {
//         return [];
//     }

//     wordFrequency = {};

//     words.forEach((word) => {
//         if (!(word in wordFrequency)) {
//             wordFrequency[word] = 0;
//         }
//         wordFrequency[word] += 1;
//     });

//     const resultIndices = [],
//         wordsCount = words.length;
//     wordLength = words[0].length;

//     for (i = 0; i < (str.length - wordsCount * wordLength) + 1; i++) {
//         const wordsSeen = {};
//         for (j = 0; j < wordsCount; j++) {
//             next_word_index = i + j * wordLength;
//             // Get the next word from the string
//             word = str.substring(next_word_index, next_word_index + wordLength);
//             if (!(word in wordFrequency)) { // Break if we don't need this word
//                 break;
//             }

//             // Add the word to the 'wordsSeen' map
//             if (!(word in wordsSeen)) {
//                 wordsSeen[word] = 0;
//             }
//             wordsSeen[word] += 1;


//             // no need to process further if the word has higher frequency than required
//             if (wordsSeen[word] > (wordFrequency[word] || 0)) {
//                 break;
//             }

//             if (j + 1 === wordsCount) { // Store index if we have found all the words
//                 resultIndices.push(i);
//             }
//         }
//     }

//     return resultIndices;
// }



console.log("RESULT ", find_word_concatenation("catfoxcat", ["cat", "fox"]))
console.log("RESULT ", find_word_concatenation("catcatfoxfox", ["cat", "fox"]))
console.log("RESULT ", find_word_concatenation("catcatfoxsheepfox", ["cat", "fox", "sheep"]))