/*Sans expresssion régulière*/

zip_code=prompt("Quel est votre zip code ??")

if(isNaN(zip_code) || zip_code == "" || zip_code == null || zip_code.indexOf(' ') >= 0 || zip_code.length>5) {
    console.log("error")
} else {
  console.log("Success")
}

/*Avec Expression régulière*/

if(zip_code.match(/\b\d{6,}\b/g) || zip_code.match(/\s/g) || /[a-zA-Z]/.test(zip_code)==true ){
    console.log("error")
}

