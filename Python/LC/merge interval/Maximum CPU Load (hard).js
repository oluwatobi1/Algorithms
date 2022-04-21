// We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when
//  it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

// Example 1:

// Jobs: [[1,4,3], [2,5,4], [7,9,6]]
// Output: 7
// Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when 
// both the jobs are running at the same time i.e., during the time interval (2,4).

// Example 2:

// Jobs: [[6,7,10], [2,4,11], [8,12,15]]
// Output: 15
// Explanation: None of the jobs overlap, therefore we will take the maximum load of any 
// job which is 15.

// Example 3:

// Jobs: [[1,4,2], [2,4,1], [3,6,5]]
// Output: 8
// Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3,4].
const Heap = require("./collections/heap");
class Job {
    constructor(start, end, cpu_load) {
        this.start = start;
        this.end = end;
        this.cpu_load = cpu_load;
    }
};

const find_max_cpu_load = function(jobs) {
    // TODO: Write your code here
    let maxLoad = 0,
        result = 0,
        minHeap = new Heap([], null, (a, b) => b.end - a.end);
    jobs.sort((a, b) => a.start - b.start)
    for (let i = 0; i < jobs.length; i++) {
        while (minHeap.length > 0 && jobs[i].start > minHeap.peek().end) {
            maxLoad -= minHeap.pop().cpu_load
        }
        minHeap.push(jobs[i])
        maxLoad += jobs[i].cpu_load
        result = Math.max(maxLoad, result)
    }
    return result;
};


console.log(`Maximum CPU load at any time: ${find_max_cpu_load(
      [new Job(1, 4, 3), new Job(2, 5, 4), new Job(7, 9, 6)])}`)
console.log(`Maximum CPU load at any time: ${find_max_cpu_load(
      [new Job(6, 7, 10), new Job(2, 4, 11), new Job(8, 12, 15)])}`)
console.log(`"Maximum CPU load at any time: ${find_max_cpu_load(
      [new Job(1, 4, 2), new Job(2, 4, 1), new Job(3, 6, 5)])}`)