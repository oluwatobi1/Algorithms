class Node {
    constructor(value, next = null) {
        this.value = value;
        this.next = next;
    }

    print_list() {
        result = "";
        temp = this;
        while (temp !== null) {
            result += temp.value + " ";
            temp = temp.next;
        }
        console.log(result);
    }
}


const reorder = function(head) {
    // TODO: Write your code here
    let fast = slow = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    };
    secondHalf = reverse(slow);
    firstHalf = head;
    while (firstHalf && secondHalf) {
        temp = firstHalf.next
        firstHalf.next = secondHalf;
        firstHalf = temp

        temp = secondHalf.next;
        secondHalf.next = firstHalf;
        secondHalf = temp;
    }
    if (firstHalf) {
        firstHalf.next = null;
    }

}

const reverse = function(head) {
    let prev = null;
    while (head) {
        next = head.next;
        head.next = prev;
        prev = head;
        head = next;
    }
    return prev
}


head = new Node(2)
head.next = new Node(4)
head.next.next = new Node(6)
head.next.next.next = new Node(8)
head.next.next.next.next = new Node(10)
head.next.next.next.next.next = new Node(12)
reorder(head)
head.print_list()