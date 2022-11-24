function isDivisible(){

    var sum=0;

    for(i=0; i<500; i++){
        if(i%23==0){
            console.log(i,"est divisible par 23")
            sum=sum+i
        }
    }
    console.log("La somme des nombres divisibles par 23 est =", sum)
}

isDivisible()