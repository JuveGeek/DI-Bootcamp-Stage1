str=prompt("Enter a word : ")

//Delete all the vowels of the word and console.log the result.
const noVowels = str.replace(/[aeiou]/gi, '');

console.log(noVowels); //

//Replace the vowels with another character and console.log the result

const newStr = str.replace(/[aeiou]/gi, 'z');

console.log(newStr); //