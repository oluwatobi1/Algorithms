// Problem Statement #
// Given a list of non-overlapping intervals sorted by their start time, insert a given
//  interval at the correct position and merge all necessary intervals to produce a list
//   that has only mutually exclusive intervals.

// Example 1:

// Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
// Output: [[1,3], [4,7], [8,12]]
// Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
// Example 2:

// Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
// Output: [[1,3], [4,12]]
// Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
// Example 3:

// Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
// Output: [[1,4], [5,7]]
// Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].


class Interval {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }

    print_interval() {
        process.stdout.write(`[${this.start}, ${this.end}]`);
    }
}

const insert = function(intervals, new_interval) {
    let merged = [];
    // TODO: Write your code here
    let i = 0;
    let start = intervals[i].start,
        end = intervals[i].end;
    while (i < intervals.length && new_interval.start > end) {
        merged.push(new Interval(start, end))
        i++
        start = intervals[i].start;
        end = intervals[i].end;
    }

    while (i < intervals.length && new_interval.end > intervals[i].start) {
        start = intervals[i].start;
        end = intervals[i].end
        start = Math.min(start, new_interval.start);
        end = Math.max(end, new_interval.end);
        i++
    }
    merged.push(new Interval(start, end))

    while (i < intervals.length) {
        start = intervals[i].start;
        end = intervals[i].end;
        merged.push(new Interval(start, end))
        i++
    }
    return merged;
};

process.stdout.write('Intervals after inserting the new interval: ');
let result = insert([
    new Interval(1, 3),
    new Interval(5, 7),
    new Interval(8, 12),
], new Interval(4, 6));
for (i = 0; i < result.length; i++) {
    result[i].print_interval();
}
console.log();

process.stdout.write('Intervals after inserting the new interval: ');
result = insert([
    new Interval(1, 3),
    new Interval(5, 7),
    new Interval(8, 12),
], new Interval(4, 10));
for (i = 0; i < result.length; i++) {
    result[i].print_interval();
}
console.log();

process.stdout.write('Intervals after inserting the new interval: ');
result = insert([new Interval(2, 3),
    new Interval(5, 7),
], new Interval(1, 4));
for (i = 0; i < result.length; i++) {
    result[i].print_interval();
}
console.log();