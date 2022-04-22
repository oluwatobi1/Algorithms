// For ‘K’ employees, we are given a list of intervals representing the working hours of 
// each employee. Our goal is to find out if there is a free interval that is common to all 
// employees. You can assume that each list of employee working hours is sorted on the start time.

// Example 1:
// Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
// Output: [3,5]
// Explanation: Both the employees are free between [3,5].

// Example 2:

// Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
// Output: [4,6], [8,9]
// Explanation: All employees are free between [4,6] and [8,9].

// Example 3:

// Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
// Output: [5,7]
// Explanation: All employees are free between [5,7].

const Heap = require('./collections/heap')
class Interval {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }

    get_interval() {
        return "[" + this.start + ", " + this.end + "]";
    }
};

class EmployeeInterval {
    constructor(interval, employeeIndex, intervalIndex) {
        this.interval = interval;
        this.employeeIndex = employeeIndex;
        this.intervalIndex = intervalIndex;
    };
};

const find_employee_free_time = function(schedule) {
    result = [];
    // TODO: Write your code here
    let n = schedule.length,
        minHeap = new Heap([], null, (a, b) => b.interval.start - a.interval.start);
    if (schedule === null || n === 0) return result;
    for (let i = 0; i < n; i++) {
        minHeap.push(new EmployeeInterval(schedule[i][0], i, 0))
    };
    const prevInterval = minHeap.peek()
    while (minHeap.length > 0) {
        const queueTop = minHeap.pop()
        if (prevInterval.interval.end < queueTop.interval.start) {
            result.push(new Interval(prevInterval.interval.end, queueTop.interval.start))
            prevInterval.interval = queueTop.interval
        } else {
            if (prevInterval.interval.end < queueTop.interval.end) {
                prevInterval.interval = queueTop.interval;
            }
        }
        const employeeSchedule = schedule[queueTop.employeeIndex];
        if (employeeSchedule.length > queueTop.intervalIndex + 1) {
            minHeap.push(new EmployeeInterval(employeeSchedule[queueTop.intervalIndex + 1], queueTop.employeeIndex,
                queueTop.intervalIndex + 1))
        }
    }
    return result;
};


input = [
    [new Interval(1, 3), new Interval(5, 6)],
    [
        new Interval(2, 3), new Interval(6, 8)
    ]
];
intervals = find_employee_free_time(input)
result = "Free intervals: ";
for (i = 0; i < intervals.length; i++)
    result += intervals[i].get_interval();
console.log(result);


input = [
    [new Interval(1, 3), new Interval(9, 12)],
    [
        new Interval(2, 4)
    ],
    [new Interval(6, 8)]
];
intervals = find_employee_free_time(input)
result = "Free intervals: ";
for (i = 0; i < intervals.length; i++)
    result += intervals[i].get_interval();
console.log(result);

input = [
    [new Interval(1, 3)],
    [
        new Interval(2, 4)
    ],
    [new Interval(3, 5), new Interval(7, 9)]
];
intervals = find_employee_free_time(input)
result = "Free intervals: ";
for (i = 0; i < intervals.length; i++)
    result += intervals[i].get_interval();
console.log(result);