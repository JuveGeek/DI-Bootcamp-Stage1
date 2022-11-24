/* Exercice 1 */
const people = ["Geg", "Mary", "Devon", "James"];

//Part 1
// 1.Supprimer "Greg"
people.shift();

// 2. Remplacer James par Jason
people[2] ="Jason"

//3.
people.push("Juvénal")

//4.
console.log(people.indexOf("Mary"))

//5.
console.log(people.slice(2))

//6.Ca retourne -1 parce que Foo n'existe pas dans le tableau people
console.log(people.indexOf("Foo"))

//7.
last = people[people.length-1]

console.log(last)

//Part 2
//1.
for(i=0;i<people.length-1;i++){
    console.log(people[i])
}

console.log("----------------------------------------------------------\n")

//2.
for(i=0;i<people.length-1;i++){
    if(people[i]=="Jason"){
        break;
    }
    console.log(people[i]);
}
