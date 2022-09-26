console.log("Running")

let nameInput = document.getElementById('name');
let ageInput = document.getElementById('age');
let emailInput = document.getElementById('email');
let dateOfBirthInput = document.getElementById('dateOfBirth');
let genderRadioButtons = document.querySelectorAll(`input[name="gender"]`);
let hobbiesInput = document.querySelectorAll(`input[name="hobbies"]:checked`);
let phoneInput = document.getElementById('phone');
let addressInput = document.getElementById('address');
let serviceInput = document.getElementById('service');
let form = document.querySelector("form");


nameInput.addEventListener("blur", (e) => {
    let letters = /^[0-9A-Za-z]+$/g;
    if (nameInput.value == "") {
        alert('Username must have not empty');
    }
    else if (nameInput.value.match(letters)) {
        return true;
    }
    
})

ageInput.addEventListener("blur", (e) => {
    if (isNaN(ageInput.value)) {
        alert("Please write a valid age");
    }
})

emailInput.addEventListener("blur", (e) => {
    if (!/[0-9a-zA-Z\.].*\@[0-9a-zA-Z].*\.(com|in)/g.test(email.value)) {
        alert("Invalid email");
    }
});


form.addEventListener("submit", (e) => {
    let genderRadioButtons = document.querySelectorAll(`input[name="gender"]`);
    let hobbiesInput = document.querySelectorAll(`input[name="hobbies"]:checked`);
    let gender = "";
    const hobbies = [];
    
    for (let radio of genderRadioButtons) {
        if (radio.checked) {
          gender = radio.value;
          break;
        }
      }

    if (gender === "") {
        alert("Please select a gender");
        e.preventDefault();
      }

    hobbiesInput.forEach((element) => {
        hobbies.push(element.value);
    });

    if(hobbies.length < 3){
        alert("Please select atleast 3 hobbies");
        e.preventDefault();
    }

});


