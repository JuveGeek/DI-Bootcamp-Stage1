function calculateTip(){
    let amount= parseInt(prompt("Quel est le montant du billlet payé"))

    if(amount<50){
        tipAmount=parseInt(amount*20/100)
        finalAmount= amount + tipAmount
    }else if(amount<200){
         tipAmount= parseInt(amount*15/100)
        finalAmount= amount + tipAmount
    }else {
        tipAmount= parseInt(amount*10/100)
        finalAmount= amount + tipAmount
    }

    console.log("The tip amount is : ", tipAmount)
    console.log("The total amount is : ", finalAmount)


}

calculateTip()