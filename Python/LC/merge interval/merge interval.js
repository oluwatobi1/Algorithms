class Interval {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }

    get_interval() {
        return "[" + this.start + ", " + this.end + "]";
    }
}


const merge = function(intervals) {
    merged = []
        // TODO: Write your code here
    if (intervals.length < 2) {
        return intervals
    }
    intervals.sort((a, b) => a.start - b.start)
    let start = intervals[0].start,
        end = intervals[0].end;
    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i].start < end) {
            merged.push(new Interval(start, end));
            merged.push(new Interval(intervals[i].start, intervals[i].end));
        }
        start = intervals[i].start;
        end = intervals[i].end;
    }

    return merged;
};

merged_intervals = merge([new Interval(1, 4), new Interval(2, 5), new Interval(7, 9)]);
result = "";
for (i = 0; i < merged_intervals.length; i++) {
    result += merged_intervals[i].get_interval() + " ";
}
console.log(`Merged intervals: ${result}`)


merged_intervals = merge([new Interval(6, 7), new Interval(2, 4), new Interval(5, 9)]);
result = "";
for (i = 0; i < merged_intervals.length; i++) {
    result += merged_intervals[i].get_interval() + " ";
}
console.log(`Merged intervals: ${result}`)


merged_intervals = merge([new Interval(1, 4), new Interval(2, 6), new Interval(3, 5)]);
result = "";
for (i = 0; i < merged_intervals.length; i++) {
    result += merged_intervals[i].get_interval() + " ";
}
console.log(`Merged intervals: ${result}`)


// Similar Problems
// Problem 1: Given a set of intervals, find out if any two intervals overlap.

// Example:
// Intervals: [[1,4], [2,5], [7,9]]
// Output: true
// Explanation: Intervals [1,4] and [2,5] overlap