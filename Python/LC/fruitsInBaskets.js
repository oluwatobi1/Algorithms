const fruits_into_baskets = function(fruits) {
    // TODO: Write your code here
    let windowSeen = {},
        windowStart = 0,
        windowEnd = 0,
        result = [];

    while (windowEnd < fruits.length + 1) {
        console.log("movement", windowStart, windowEnd);
        windowSeen[fruits[windowEnd]] = (windowSeen[fruits[windowEnd]] || 0) + 1
        if (Object.keys(windowSeen).length <= 2) {
            if (windowEnd - windowStart + 1 > result.length && Object.keys(windowSeen).length === 2) {
                result = fruits.slice(windowStart, windowEnd + 1);
            }
        } else {
            let leftFruit = fruits[windowStart]
            windowSeen[leftFruit] -= 1
            if (windowSeen[leftFruit] === 0) {
                delete windowSeen[leftFruit];
            };
            windowStart += 1
        };
        windowEnd += 1
    };
    return result;
};


console.log(`Maximum number of fruits: ${fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])}`);
console.log(`Maximum number of fruits: ${fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])}`);