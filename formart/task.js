let age = prompt("Enter the value of your age:");
age = Number.parseInt(age);

let output = "Your age is " + age;
let output1 = "";
let output2 = "";
let output3 = "";

if (!isNaN(age)) {
    if (age > 18 && age <= 21) {
        output1 = "You are a teenager, so you can drink in moderation.";
    } else if (age > 21) {
        output2 = "You are legally allowed to drink.";
    } else {
        output3 = "You are not old enough to drink.";
    }
} else {
    output = "Please enter a valid age.";
}

document.getElementById("output").innerHTML = output;
document.getElementById("output1").innerHTML = output1;
document.getElementById("output2").innerHTML = output2;
document.getElementById("output3").innerHTML = output3;
