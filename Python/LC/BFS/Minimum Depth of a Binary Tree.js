// Find the minimum depth of a binary tree. The minimum depth is the number of 
// nodes along the shortest path from the root node to the nearest leaf node.



class TreeNode {

    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
};


const find_minimum_depth = function(root) {
    // TODO: Write your code here
    let result = 1;
    let queue = [root];
    while (queue.length > 0) {
        let levelSize = queue.length;
        let right = true,
            left = true;
        for (let i = 0; i < levelSize; i++) {
            currLeaf = queue.shift()
            if (currLeaf.left) {
                queue.push(currLeaf.left)
                left = true
            } else {
                left = false
            }
            if (currLeaf.right) {
                queue.push(currLeaf.right)
                right = true
            } else {
                right = false
            }
            if (!right && !left) {
                return result
            }
        }
        result += 1
    }
    return result;
};



var root = new TreeNode(12)
root.left = new TreeNode(7)
root.right = new TreeNode(1)
root.right.left = new TreeNode(10)
root.right.right = new TreeNode(5)
console.log(`Tree Minimum Depth: ${find_minimum_depth(root)}`)
root.left.left = new TreeNode(9)
root.right.left.left = new TreeNode(11)
console.log(`Tree Minimum Depth: ${find_minimum_depth(root)}`)