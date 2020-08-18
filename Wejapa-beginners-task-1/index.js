function jazzify(arr){
  let out = [];
 for (let i= 0;i<arr.length;i++){
    let item = arr[i]
    if (item[item.length-1] !== "7"){
      out.push(item+"7")
    }else{
      out.push(item);
    }
  }return out
}

function marathonDistance(ls){
  let re = ls.reduce((a, b)=> (Math.abs(a)+Math.abs(b)))
  return re===25
}

function arrayOfMultiples(num,le){
  let out = []
  
  for (let i= 1;i<=le;i++){
    out.push(num*i)
  }
  return out
}


function ts(){
  return ("2020-08-04T13:34:42.351")

}

function thedate(fn){
  let map = {}
  dt= new fn()
  dt= String(dt);
  fdate = dt.split("T")[0];
  map["year"]= fdate.split("-")[0]
  map["day"]= fdate[1];
  map["month"]= fdate[2];
return map
}

thedate(ts)

