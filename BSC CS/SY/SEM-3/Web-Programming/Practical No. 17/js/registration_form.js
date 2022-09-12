// function validate() {
//     if (allLetter(name)) {
//         if (alphanumeric(address)) {

//         }

//     }


//     if (isNaN(age)) {
//         alert("Please write a valid age");
//     }

//     else if (isNaN(phone)) {
//         alert("Please write a valid phone number");
//     }


// }

let name = document.getElementById('name').value;
let age = document.getElementById('age').value;
let email = document.getElementById('email').value;
let dateOfBirth = document.getElementById('dateOfBirth').value;
let hobbies = document.getElementById('hobbies').value;
// let phoneOptions = document.getElementById('phoneOptions').value;
let phone = document.getElementById('phone').value;
let address = document.getElementById('address').value;
// let countryOptions = document.getElementById('countryOptions').value;
let service = document.getElementById('service').value;

function allLetter() {
    let letters = /^[A-Za-z]+$/;
    if (name.value == "") {
        alert('Username must have not empty');
    }
    else if (name.value.match(letters)) {
        return true;
    }
    else {
        alert('Username must have alphabet characters only');
        name.focus();
        return false;
    }
}

function age() {
    let age = document.getElementById('age').value;
    if (isNaN(age)) {
         alert("Please write a valid age");
    }       
}

// function alphanumeric(uadd) {
//     var letters = /^[0-9a-zA-Z]+$/;
//     if (uadd.value.match(letters)) {
//         return true;
//     }
//     else {
//         alert('User address must have alphanumeric characters only');
//         uadd.focus();
//         return false;
//     }
// }