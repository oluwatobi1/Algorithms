class Stack {
    constructor() {
        this.stack = [];
    }

    push(data) {
        this.stack.push(data)
    };
    pop() {
        this.stack.pop()
    }
}


let myStack = new Stack();
myStack.push(3);
myStack.push(3);
myStack.push(5);
myStack.push(2);
myStack.push(8);

console.log("Stack is ", myStack.stack)
myStack.pop()
console.log("Stack is ", myStack.stack)