// Right View of a Binary Tree (easy)#
// Given a binary tree, return an array containing nodes in its right view.
//  The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.

class TreeNode {

    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
};

const tree_right_view = function(root) {
    result = [];
    // TODO: Write your code here
    let queue = [root]
    while (queue.length > 0) {
        let levelSize = queue.length
        for (let i = 0; i < levelSize; i++) {

            let currLeaf = queue.shift()
            if (i === levelSize - 1) {
                result.push(currLeaf.value)
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


var root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
root.left.left.left = new TreeNode(3);
console.log("Tree right view: " + tree_right_view(root))