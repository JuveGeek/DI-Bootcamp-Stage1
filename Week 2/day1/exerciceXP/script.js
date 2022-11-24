/*exercice 1*/

favorite_food="pomme"
favorite_meal="dinner"

console.log("I eat ",favorite_food," ","at every",favorite_meal)

/*exercice 2*/
const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

let myWatchedSeriesLength = myWatchedSeries.length

let myWatchedSeriesSentence = "black mirror, money heist, and the big bang theory"

console.log("I watched", myWatchedSeriesLength,"series : ", myWatchedSeriesSentence)

myWatchedSeries[2]="friends"

myWatchedSeries.push("bingo")

myWatchedSeries.unshift("Les malheurs de Sofie")

myWatchedSeries.splice(1,1)

console.log("money heist".charAt(2))

console.log(myWatchedSeries)

/*exercice 3*/
let celsiusTemp=20
let fahrenheitTemp;

console.log(celsiusTemp,"°C", "is", ((celsiusTemp/5*9)+32), "°F")

/*exercice 4*/

let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// 55 parce que 34 et 21 sont des nombres:
// 55:

a = 2;

console.log(a+b) //second expression
// 23 parce que a prend la valeur de 2:
// 23:

console.log(3 + 4 + '5');
//Ca donnera 75 parce 3+4=7 puis on concatène à 5 qui est une chaîne de caractère

/*exercice 5*/
console.log(typeof(15))
// Int: parce que c'est un entier
// Actual: number

console.log(typeof(5.5))
// Double : parce que c'est un décimal:
// Actual: number

console.log(typeof(NaN))
// Prediction:null
// Actual:number

console.log(typeof("hello"))
// Prediction:string
// Actual:string

console.log(typeof(true))
// Prediction: boolean
// Actual:boolean

console.log(typeof(1 != 2))
// Prediction: boolean
// Actual:boolean

console.log("hamburger" + "s")
// Prediction: hambergers
// Actual: hambergers

console.log("hamburgers" - "s")
// Prediction: hamberger
// Actual:NaN

console.log("1" + "3")
// Prediction:13
// Actual:13

console.log("1" - "3")
// Prediction:31
// Actual:-2

console.log("johnny" + 5)
// Prediction:johnny5
// Actual:johnny5

console.log("johnny" - 5)
// Prediction:NaN
// Actual:NaN

console.log(99 * "hello")
// Prediction: hello 99 fois
// Actual:

console.log(1 != 1)
// Prediction:false
// Actual:

console.log(1 == "1")
// Prediction: false
// Actual:true

console.log(1 === "1")
// Prediction:false
// Actual:false
console.log("-------------------------------------------------------------------")

console.log(5 + "34")
// Prediction:
// Actual:

console.log(5 - "4")
// Prediction:
// Actual:

console.log(10 % 5)
// Prediction:
// Actual:

console.log(5 % 10)
// Prediction:
// Actual:

console.log("Java" + "Script")
// Prediction:
// Actual:

console.log(" " + " ")
// Prediction: 
// Actual: 

console.log(" " + 0)
// Prediction: 0
// Actual: 0

console.log(true + true)
// Prediction: 2 : false=0 et true=1
// Actual: 2

console.log(true + false)
// Prediction:1: false=0 et true=1
// Actual:1

console.log(false + true)
// Prediction: 1: false=0 et true=1
// Actual:  1

console.log(false - true)
// Prediction: -1 : false=0 et true=1
// Actual: -1

console.log(!true)
// Prediction: fals
// Actual:false

console.log(3 - 4)
// Prediction:-1
// Actual:-1

console.log("Bob" - "bill")
// Prediction: NaN : pas un nombre
// Actual: NaN