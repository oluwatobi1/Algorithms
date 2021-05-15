function generatePermutations(perm:Number[], n: Number):void{
    if (perm.length == n){
        console.log(perm);
        return        
    }

    for (let k=0; k<n;k++){
        if (perm.indexOf(k)<0) {
            perm.push(k)
            generatePermutations(perm,n)
            perm.pop()
        }
    }
}

generatePermutations([], 3)
