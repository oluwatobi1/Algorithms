function spiralCopy(inputMatrix) {
    // your code goes here
    result = [];
    let maxHeight = inputMatrix.length - 1,
        maxWidth = inputMatrix[0].length - 1;
    let horizontal = true,
        vertical = false;
    let i = 0,
        j = 0,
        end = (maxHeight + 1) * (maxWidth + 1);
    let startRow = false,
        startCol = false,
        switcher = 1;
    let rowEnd = 0,
        colEnd = 0;

    console.log('maxHeight', maxHeight, maxWidth)
    if (inputMatrix.length == 1) {
        return inputMatrix[0]
    }

    while (end > 0) {
        console.log('here', "j", j, "maxwidth", maxWidth, "i", i, "maxHeight", maxHeight, "colEnd", colEnd, "rowEnd", rowEnd, end, 'vertical', vertical, 'horiz', horizontal)
        result.push(inputMatrix[i][j])
        console.log(result)

        if (i === maxHeight && startCol === false && (j !== maxWidth || j !== rowEnd)) {
            horizontal = !horizontal;
            vertical = !vertical;
            maxHeight -= 1;
            switcher = -1;
            startCol = true;
            console.log('flip 1')

        } else if (j === maxWidth && startRow === false && (i === maxHeight || i === colEnd)) {
            horizontal = !horizontal;
            vertical = !vertical;
            console.log('flip 2')
            startRow = true;
            colEnd += 1
        } else if (j === rowEnd && startRow === true && (i === maxHeight || i === colEnd)) {
            horizontal = !horizontal;
            vertical = !vertical;
            maxWidth -= 1;
            console.log('flip 3')
            rowEnd += 1;
            startRow = false;
        } else if (i === colEnd && startCol === true && (j === maxWidth || j === rowEnd)) {
            horizontal = !horizontal;
            vertical = !vertical;
            startCol = false;
            switcher = 1;
            console.log('flip 4')

        }

        if (horizontal) {
            j += switcher
        } else {
            i += switcher
        }
        end--;
    }
    return result
}

function spiralMatrix(matrix) {
    let row = matrix.length - 1,
        col = matrix[0].length - 1;
    let top = 0,
        bottom = row,
        left = 0,
        right = col;

    let dir = 0,
        result = [];

    while (top <= bottom && left <= right) {
        console.log('result', result)
        if (dir == 0) {
            for (let i = left; i < right + 1; i++) {
                result.push(matrix[top][i])
            }
            top += 1;
            dir = 1;
            console.log('flip 1')
        } else if (dir === 1) {
            for (let i = top; i < bottom + 1; i++) {
                result.push(matrix[i][right])
            }
            right -= 1;
            console.log('flip 2')
            dir = 2
        } else if (dir === 2) {
            for (let i = right; i > left - 1; i--) {
                result.push(matrix[bottom][i])
                console.log("matrix", matrix[bottom][i]);
            }
            bottom -= 1;
            dir = 3;
        } else if (dir === 3) {
            for (let i = bottom; i > top - 1; i--) {
                result.push(matrix[i][left])
            }
            left += 1
            dir = 0
        }
    }
    return result
}

console.log(spiralMatrix([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]))


// console.log(spiralCopy([
//     [1, 2, 3, 4, 5],
//     [6, 7, 8, 9, 10],
//     [11, 12, 13, 14, 15]
// ]))