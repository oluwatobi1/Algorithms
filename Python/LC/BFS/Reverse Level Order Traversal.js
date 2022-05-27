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
        result.unshift(temp)
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