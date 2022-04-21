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

class Interval {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }

    get_interval() {
        return "[" + this.start + ", " + this.end + "]";
    }
};

const find_employee_free_time = function(schedule) {
    result = [],
        temp = [];
    for (let i = 0; i < schedule.length; i++) {
        for (let j = 0; j < schedule[i].length; j++) {
            temp.push(schedule[i][j]);
        }
    }
    temp.sort((a, b) => a.start - b.start);
    for (let i = 1; i < temp.length; i++) {
        if (temp[i].start > temp[i - 1].end) {
            result.push(new Interval(temp[i - 1].end, temp[i].start))
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