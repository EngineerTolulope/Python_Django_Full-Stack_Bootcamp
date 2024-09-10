var firstName = prompt("First name please: ")
var lastName = prompt("Last name please: ")
var age = prompt("How old are you?")
var height = prompt("What is your height?")
var petName = prompt("What is your pet name?")
alert("Thank you so much for the information!")


var nameCond = false;
var ageCond = false;
var heightCond = false;
var petCond = false;


if (firstName[0] === lastName[0]){
  nameCond = true;
}

if (age > 20 && age < 30){
  ageCond = true;
}

if (height >= 170){
  heightCond = true;
}

if (petName[petName.length - 1] === 'y'){
  petCond = true;
}

if (nameCond && ageCond && heightCond && petCond){
  console.log("What's up spy!");
} else {
  console.log("Nothing to see here");
}
