class TreeNode {

    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
};


const traverse = function(root) {
    result = [
        [root]
    ];
    ans = [
            [root.value]
        ]
        // TODO: Write your code here
    let node = root,
        i = 0;
    while (i < result.length) {
        let arr = [],
            temp = [];
        for (let j = 0; j < result[i].length; j++) {
            let curr_node = result[i][j];
            if (curr_node.left) {
                arr.push(curr_node.left)
                temp.push(curr_node.left.value)
            }
            if (curr_node.right) {
                arr.push(curr_node.right);
                temp.push(curr_node.right.value)
            }
        }
        console.log('ans', ans)
        if (arr.length > 0) {
            result.push(arr);
            ans.push(temp)
        }
        i++;
    }
    return ans;
};



var root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(18);
root.right.right.right = new TreeNode(5);
root.right.right.right.right = new TreeNode(4);
root.right.right.right.left = new TreeNode(54);
root.right.right.right.left.right = new TreeNode(78);
root.right.right.right.left.right.left = new TreeNode(78);
root.right.right.right.left.right.left.right = new TreeNode(78);
console.log(`Level order traversal: ${traverse(root)}`);