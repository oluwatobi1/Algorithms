const arr = [2, 3, 6, 8, 3, 6]

const ss = function(arr) {
    let result = [];
    for (let i = arr.length - 1; i > 0; i--) {
        const tempList = new Array();
        tempList.unshift(arr[i])
        result.push(tempList)
        console.log("tempList", tempList, "result", result);
    };
    return result
}

console.log("result", ss(arr));