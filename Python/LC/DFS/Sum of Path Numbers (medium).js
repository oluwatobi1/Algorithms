// Given a binary tree where each node can only have a digit (0-9) value, 
// each root-to-leaf path will represent a number. Find the total sum of all
//  the numbers represented by all paths.


class TreeNode {

    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
};


const find_sum_of_path_numbers = function(root) {
    // TODO: Write your code here
    let sum = [0];
    find_dfs(root, sum)
    return sum[0];
};

const find_dfs = function(root, sum, currentSum = 0) {;
    if (root == null) {
        return;
    }
    currentSum = (currentSum * 10) + root.value;

    if (root.left === null && root.right === null) {
        sum[0] += currentSum
    } else {
        find_dfs(root.left, sum, currentSum)
        find_dfs(root.right, sum, currentSum)
    }
    currentSum = (currentSum - root.value) / 10


}



var root = new TreeNode(1)
root.left = new TreeNode(0)
root.right = new TreeNode(1)
root.left.left = new TreeNode(1)
root.right.left = new TreeNode(6)
root.right.right = new TreeNode(5)
console.log(`Total Sum of Path Numbers: ${find_sum_of_path_numbers(root)}`)