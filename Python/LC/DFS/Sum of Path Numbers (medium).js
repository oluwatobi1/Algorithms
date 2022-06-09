class TreeNode {

    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
};


const find_sum_of_path_numbers = function(root) {
    return dfs_path(root)
};

const dfs_path = function(root, currSum = 0) {
    if (root === null) {
        return 0
    }

    currSum = (currSum * 10) + root.value
    if (root.left == null && root.right == null) {
        return currSum
    }
    return dfs_path(root.left, currSum) + dfs_path(root.right, currSum)
}



var root = new TreeNode(1)
root.left = new TreeNode(0)
root.right = new TreeNode(1)
root.left.left = new TreeNode(1)
root.right.left = new TreeNode(6)
root.right.right = new TreeNode(5)
console.log(`Total Sum of Path Numbers: ${find_sum_of_path_numbers(root)}`)