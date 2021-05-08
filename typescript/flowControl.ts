let numb :number = 12
// single statement if
if (numb <6 ) console.log("number is lesser");
else if (numb >6 && numb <8){
console.log( "number is within 6 & 8");
}else {
    console.log("number is above 8");    
}

// nested if statements

let val1 = 45
let val2 = 75

let operator = '>'

if (operator == ">"){
    console.log("Greater than ");
    
    if (val1 > val2){
        console.log("val1 is greater");
        
    }else{
        console.log("val1 <= ");
        
    }
}else if (operator == "<"){
    console.log("Less than");
    
    if (val1 < val2) {
        console.log("Val1 < val2");
        
    }else {
        console.log("Val1>= Val2");
            }

}else{
    console.log("Val1 == Val2");
    
}

//  Switch statements
let val3= 12
let val4 = 45
console.log("Switch Start");

let sign = '-'
switch (sign){
    case "+":
        console.log(val3+val4);
        break
    case "-":
        console.log(val3-val4);
        break
    case "*":
        console.log(val3*val4);
        break
    case "/":
        console.log(val3/val4);
        break
    default:
        console.log("Invalid Operator");
        
        
console.log("Switch End");

        
        
}

enum VehicleType {
    car,
    plane,
    boat,
}

let veh:number = VehicleType.car

switch (+veh){
    case VehicleType.car:
        console.log("This is a car");
        break;
    case VehicleType.boat:
        console.log("This a boat");
        break;
    case VehicleType.boat:
        console.log("This is a boat");
        break;
    default:
        console.log("Not a Vehicle");        
}

// while and do
let i = 0
while (i<5){
    console.log(i);
    i++
    
}
let k = 100

do {
    console.log(k);
    k++
    
}while (k<105)

let j = 90

do {
    console.log(j);
    j++
    if (j >100){
        break
    }
    
}while (true)

// for loops

for (let i=0; i<5;i++){
    console.log("this is "+i);
    
}

let io = 0
for (;;io++){
    if (io <2) continue;
    console.log("io "+ io);
    if (io >4){
        break
    }
    
}

// labeling loops

outerloop: for (let o =1; o<7;o++){
    innerloop: for (let p = 2;p<6;p++){
        console.log(o, p);
        
        if (o==4){
            break outerloop
        }
    }
}
