const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

//1.
names.sort()

var namo=""

for(i=0; i<names.length; i++){
    for(j=0; j<names[i].length; j++){
       // console.log(names[i][0])
       namo=namo+names[i][0]
        break
       
    }
}

console.log("Le nom de la compagnie est : ",namo)