currentYear=2022;

use1=currentYear-prompt("Quel est ton année de naissance ?? utilisateur 1")

console.log(use1)

use2=currentYear-prompt("Quel est ton année de naissance ?? utilisateur 2")


let younger;
let half;
let sol;

if (use1<use2){
    younger=use1
    half=use2/2
    sol=half-use1
   

    console.log("L'utilisateur 1 qui est le plus jeune aura la moitié de l'age du plus vieux en", use1+sol+currentYear)
}
else{
    younger=use2
    half=user1/2
    sol=half-use2
   

    console.log("L'utilisateur 2 qui est le plus jeune aura la moitié de l'age du plus vieux en", use2+sol+currentYear)
}