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
        console.log('here', "j", j, "maxwidth", maxWidth, "i", i, "maxHeight", maxHeight, "colEnd", colEnd, "rowEnd", rowEnd, end)
        result.push(inputMatrix[i][j])
        console.log(result)

        if (i === maxHeight && startCol === false) {
            horizontal = !horizontal;
            vertical = !vertical;
            maxHeight -= 1;
            switcher = -1;
            startCol = true;
            console.log('flip 1')

        } else if (j === maxWidth && startRow === false) {
            horizontal = !horizontal;
            vertical = !vertical;
            console.log('flip 2')
            startRow = true;
            colEnd += 1
        } else if (j === rowEnd && startRow === true) {
            horizontal = !horizontal;
            vertical = !vertical;
            maxWidth -= 1;
            console.log('flip 3')
            rowEnd += 1;
            startRow = false;
        } else if (i === colEnd && startCol === true) {
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

function flipDirection(direction) {

}

console.log(spiralCopy([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]))