convertTimeString = function(timeString) {
    let str, currdate, result;
    str = timeString.split(":")
    currdate = new Date()
    console.log('str', str)
    result = currdate.setHours(str[0], str[1])
    return result
};
let result = convertTimeString("23:00")

console.log("result", result)

revertTimeString = function(time) {
    let str, date = new Date(time);
    let hours = String(date.getHours()).padStart(2, '0')
    let minutes = String(date.getMinutes()).padStart(2, '0')
    str = hours + ":" + minutes
    return str
}
console.log('reverse', revertTimeString(result));


// const formatGetRestrictionDataResponse = (data) => {
//     let result = [],
//         keys = Object.keys(data);
//     for (i = 0; i < keys.length; i++) {
//         let temp = {}
//         temp['day'] = keys[i]
//         temp['times'] = data[keys[i]]
//         result.push(temp);
//     }
//     return result
// };

// console.log(
//     formatGetRestrictionDataResponse({
//         "MON": [{
//                 "end": "08:00",
//                 "start": "05:00"
//             },
//             {
//                 "end": "04:00",
//                 "start": "06:00"
//             }
//         ],
//         "TUE": [{
//                 "end": "03:00",
//                 "start": "05:00"
//             },
//             {
//                 "end": "04:00",
//                 "start": "06:00"
//             }
//         ]
//     }));