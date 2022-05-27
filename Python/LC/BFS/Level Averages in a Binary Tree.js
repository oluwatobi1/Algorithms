// Given a binary tree, populate an array to represent the averages of all of its levels.

class TreeNode {

    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
};

const find_level_averages = function(root) {
    result = [];
    // TODO: Write your code here
    let queue = [root]
    while (queue.length > 0) {
        let levelSize = queue.length;
        let mean = 0;

        for (let i = 0; i < levelSize; i++) {
            let currNode = queue.shift()
            mean += currNode.value
            if (currNode.right) {
                queue.push(currNode.right)
            }
            if (currNode.left) {
                queue.push(currNode.left)
            }

        }
        result.push(mean / levelSize)

    }
    return result;
};


var root = new TreeNode(12)
root.left = new TreeNode(7)
root.right = new TreeNode(1)
root.left.left = new TreeNode(9)
root.left.right = new TreeNode(2)
root.right.left = new TreeNode(10)
root.right.right = new TreeNode(5)

console.log(`Level averages are: ${find_level_averages(root)}`)