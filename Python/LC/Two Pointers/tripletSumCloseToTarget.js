const triplet_sum_close_to_target = function(arr, target_sum) {
    // TODO: Write your code here
    let diff = Infinity
    arr.sort((a, b) => a - b)
    for (let i = 0; i < arr.length; i++) {
        if (i > 0 && arr[i] == arr[i - 1]) continue
        search_triplets(arr, arr[i], i + 1, target_sum, diff)
    }
    return diff;
};

const search_triplets = function(arr, curr, left, target_sum, diff) {
    let right = arr.length - 1
    while (left < right) {
        let currSum = arr[left] + arr[right] + curr,
            gap = Math.abs(target_sum - currSum);
        console.log("gap", gap, "currSum", currSum, 'targetSum', target_sum);
        console.log("left", left, "right", right, 'curr', curr);

        console.log('diff', diff, "gap", gap, 'min', Math.min(diff, gap));
        diff = Math.min(diff, gap)
        if (diff > gap) {
            right -= 1
        } else if (diff < gap) {
            left += 1
        } else {
            left += 1;
            right -= 1;
        }
    }
}


console.log(triplet_sum_close_to_target([-2, 0, 1, 2], 2));
console.log(triplet_sum_close_to_target([-3, -1, 1, 2], 1));
console.log(triplet_sum_close_to_target([1, 0, 1, 1], 100));