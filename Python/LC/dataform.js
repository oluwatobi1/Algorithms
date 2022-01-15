let data1 = {
    MON: [{
            end: '08:00',
            start: '05:00'
        },
        {
            end: '04:00',
            start: '06:00'
        }
    ],
    TUE: [{
            end: '03:00',
            start: '05:00'
        },
        {
            end: '04:00',
            start: '06:00'
        }
    ]
}

const addNewTime = (data, day) => {
    data[day] = [{ end: null, start: null }].concat(data[day] || [])
    return data
}
console.log('data', data1);
console.log(addNewTime(data1, "MON"));

console.log(addNewTime(data1, "TUE"));
console.log(addNewTime(data1, "WED"));