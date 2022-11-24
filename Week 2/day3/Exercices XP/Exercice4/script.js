//1.
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

//2.
console.log("Nunber of floors is :", building.numberOfFloors)

//3.
console.log("Nimber of appartement in the flooor 1 is : ", building.numberOfAptByFloor.firstFloor)
console.log("Nimber of appartement in the flooor 3 is : ", building.numberOfAptByFloor.thirdFloor)

//4.
console.log("The name of the second tenant is : ", building.nameOfTenants[1], "and the numbre of rooms he has in his appart is :", building.numberOfRoomsAndRent.dan[0])

//5.
if((building.numberOfRoomsAndRent.sarah[1]+building.numberOfRoomsAndRent.david[1]) > building.numberOfRoomsAndRent.dan[1]){
    console.log("the sum of Sarah’s and David’s rent is bigger than Dan’s rent")

    building.numberOfRoomsAndRent.dan[1]=building.numberOfRoomsAndRent.dan[1]+1200
}
else{
    console.log("the sum of Sarah’s and David’s rent is not bigger than Dan’s rent")
}