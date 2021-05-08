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

