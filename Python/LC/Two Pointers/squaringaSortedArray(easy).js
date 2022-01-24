// Given a sorted array, create a new array containing squares of all the numbers of 
// the input array in the sorted order.

// Input: [-2, -1, 0, 2, 3]
// Output: [0, 1, 4, 4, 9]

// Input: [-3, -1, 0, 1, 2]
// Output: [0, 1, 1, 4, 9]


const make_squares = function(arr) {
    let squares = []
    if (arr.length === 0) {
        return squares
    }
    // TODO: Write your code here
    let midPoint = 0
    while (arr[midPoint] < 0) {
        midPoint += 1;
    };
    let left = midPoint,
        right = midPoint;
    console.log("left", left, "right", right);
    while (left >= 0 && right <= arr.length) {
        leftSqr = arr[left] ** 2
        rightSqr = arr[right] ** 2
        if (left == right) {
            squares.push(leftSqr)
        } else if (leftSqr > rightSqr) {
            squares.push(rightSqr)
            squares.push(leftSqr)
        } else {
            squares.push(leftSqr)
            squares.push(rightSqr)
        }
        left -= 1;
        right += 1;
    }
    return squares;
};

console.log(`Squares: ${make_squares([-2, -1, 0, 2, 3])}`);
console.log(`Squares: ${make_squares([-3, -1, 0, 1, 2])}`);
console.log(`Squares: ${make_squares([])}`);