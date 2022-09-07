function validate() {
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

    if (isNaN(age)){
        alert("Please write a valid age");
    }

    else if (isNaN(phone)){
        alert("Please write a valid phone number");
    }


}