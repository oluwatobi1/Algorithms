class TreeNode {

    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
};


const find_minimum_depth = function(root) {
    // TODO: Write your code here
    let result = 0;
    let queue = [root];
    while (queue.length > 0) {
        result += 1
        let levelSize = queue.length;
        for (let i = 0; i < levelSize; i++) {
            currLeaf = queue.shift()
            if (!currLeaf.left && !currLeaf.right) {
                return result
            }
            if (currLeaf.left) {
                queue.push(currLeaf.left)

            }
            if (currLeaf.right) {
                queue.push(currLeaf.right)
            }
        }
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