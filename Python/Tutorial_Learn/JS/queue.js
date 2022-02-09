class Que {
    constructor() {
        this.queue = []
    }
    enqueue(data) {
        this.queue.push(data)
    };
    dequeue() {
        this.queue.shift()
    };

};

myQue = new Que();
myQue.enqueue(3)
myQue.enqueue(5)
myQue.enqueue(8)
myQue.enqueue(1)

console.log("where ", myQue.queue)
myQue.dequeue()
myQue.dequeue()
console.log("where ", myQue.queue)