// Given a binary tree and a number ‘S’, find all paths from root-to-leaf such
//  that the sum of all the node values of each path equals ‘S’.

class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
};


const find_paths = function(root, sum) {
    allPaths = [];
    find_paths_recursive(root, sum, [], allPaths)
        // TODO: Write your code here
    return allPaths;
};

const find_paths_recursive = function(root, sum, currentPath, allPaths) {
    if (root == null) {
        return;
    }
    currentPath.push(root.value);
    if (root.left == null && root.right == null && root.value == sum) {
        allPaths.push(currentPath);
    } else {
        find_paths_recursive(root.left, sum - root.val, currentPath, allPaths);
        find_paths_recursive(root.right, sum - root.val, currentPath, allPaths);
    }

    currentPath.pop(root.value);
};



var root = new TreeNode(12)
root.left = new TreeNode(7)
root.right = new TreeNode(1)
root.left.left = new TreeNode(4)
root.right.left = new TreeNode(10)
root.right.right = new TreeNode(5)
sum = 23
console.log(`Tree paths with sum: ${sum}: ${find_paths(root, sum)}`)