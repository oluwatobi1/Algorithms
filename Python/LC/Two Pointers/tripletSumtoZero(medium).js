const search_triplets = function(arr) {
    triplets = [];
    arr.sort((a, b) => a - b)
    for (let i = 0; i < arr.length; i++) {
        if (i > 0 && arr[i] == arr[i - 1]) continue;
        search_pair(arr, -arr[i], i + 1, triplets)
    }
    // TODO: Write your code here
    return triplets;
};

const search_pair = function(arr, target_sum, left, triplets) {
    let right = arr.length - 1;
    while (left < right) {
        currSum = arr[right] + arr[left];
        if (target_sum == currSum) {
            triplets.push([-target_sum, arr[left], arr[right]])
            right -= 1;
            left += 1;
            while (left < right && arr[left] == arr[left - 1]) {
                left += 1
            }
            while (left < right && arr[right] == arr[right + 1]) {
                right -= 1
            }
        } else if (currSum > target_sum) {
            right -= 1
        } else {
            left += 1
        }
    }
}


console.log(search_triplets([-3, 0, 1, 2, -1, 1, -2]));
console.log(search_triplets([-3, 4, -2, -2, 0, 1, 2, -1, 1, -2]));
console.log(search_triplets([-5, 2, -1, -2, 3]));