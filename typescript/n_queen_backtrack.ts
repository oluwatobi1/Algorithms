function can_extend_to_solution(perm:number[]):boolean{
    let k = perm.length - 1
    for (let i=0; i<k; i++){
        if ((k-i) == Math.abs(perm[k]-perm[i])){
            return false
        }
    }return true

}

function extend(perm:number[], n: number):void{
    if (perm.length == n){
        console.log(perm);
        return        
    }

    for (let k=0; k<n;k++){
        if (perm.indexOf(k)<0) {
            perm.push(k)
            if (can_extend_to_solution(perm)){
                extend(perm,n)
            }
            perm.pop()
        }
    }
}

extend([], 4)
