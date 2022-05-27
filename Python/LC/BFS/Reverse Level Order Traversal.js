// Given a binary tree, populate an array to represent its 
// level-by-level traversal in reverse order, i.e., the lowest level comes first. 
// You should populate the values of all nodes in each level from 
// left to right in separate sub-arrays.

class TreeNode {

    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
};

const traverse = function(root) {
    result = [];
    // TODO: Write your code here
    queue = [root]
    while (queue.length > 0) {
        let levelSize = queue.length
        let temp = []
        for (let i = 0; i < levelSize; i++) {
            let currNode = queue.shift()
            temp.push(currNode.value)
            if (currNode.left) {
                queue.push(currNode.left)
            }
            if (currNode.right) {
                queue.push(currNode.right)
            }
        }
        result.push(temp)

    }
    let pointer1 = 0,
        pointer2 = result.length - 1;
    while (pointer1 < pointer2) {
        [result[pointer1], result[pointer2]] = [result[pointer2], result[pointer1]];
        pointer1 += 1
        pointer2 -= 1
    }
    return result;
}

var root = new TreeNode(12)
root.left = new TreeNode(7)
root.right = new TreeNode(1)
root.left.left = new TreeNode(9)
root.right.left = new TreeNode(10)
root.right.right = new TreeNode(5)
console.log(`Reverse level order traversal: ${traverse(root)}`)