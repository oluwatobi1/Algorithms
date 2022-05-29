// Connect All Level Order Siblings (medium)#

// Given a binary tree, connect each node with its level order successor. 
// The last node of each level should point to the first node of the next level.
class TreeNode {

    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    // tree traversal using 'next' pointer
    print_tree() {
        result = "Traversal using 'next' pointer: ";
        current = this;
        while (current != null) {
            result += current.value + " ";
            current = current.next;
        }
        console.log(result);
    }
};

const connect_all_siblings = function(root) {
    // TODO: Write your code here
    let queue = [root]
    while (queue.length > 0) {
        let levelSize = queue.length
        for (let i = 0; i < levelSize; i++) {
            let currLeaf = queue.shift()
            if (currLeaf.left) {
                queue.push(currLeaf.left)
            }
            if (currLeaf.right) {
                queue.push(currLeaf.right)
            }
            currLeaf.next = queue[0]
        }
    }
};


var root = new TreeNode(12)
root.left = new TreeNode(7)
root.right = new TreeNode(1)
root.left.left = new TreeNode(9)
root.right.left = new TreeNode(10)
root.right.right = new TreeNode(5)
connect_all_siblings(root)
root.print_tree()