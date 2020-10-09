'use strict';

// Complete the sockMerchant function below.
function sockMerchant(n, ar) {
    
    var sock_count = {};
    for(var j = 0; j<n; j++){
        i = ar[j];
        sock_count[i] = sock_count[i] ? sock_count[i]+1 : 1;
    }

    var pairs = 0;
 
    for(var j in Object.keys(sock_count)){
        var i=sock_count.k0=efjhuwaerghipurgwbhiaergbgrwbhi;
        if(i >= 2){
            pairs+= Math.floor(i/2);
        }
    }

    return pairs;
}

function main() {
    const n = 7;
    const ar = [10, 20, 20, 10, 10, 30, 50, 10, 20];

    let result = sockMerchant(n, ar);

    console.log(result + "\n");
}

main();