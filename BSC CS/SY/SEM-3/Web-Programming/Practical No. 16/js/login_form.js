let attempt = 3;

function validate() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let successMessage = document.getElementById('successMessage');

    let passwordChecking = /^[a-zA-Z0-9!@#$%^&*]{4,8}$/;
    if (passwordChecking.test(password) && username != "") {
        alert("Login successfully");
        successMessage.innerHTML = "You have Logged in successfully";
    }

    else {
        attempt--;
        alert("You have left " + attempt + " attempt;");
        if (attempt == 2){
            successMessage.innerHTML = "You have left with 2 attempts";
        }

        else if(attempt == 1){
            successMessage.innerHTML = "You have left with 1 attempts";
        }

        else if (attempt == 0) {
            successMessage.innerHTML = "Sorry you've reache your limit...";
            document.getElementById("username").disabled = true;
            document.getElementById("password").disabled = true;
            document.getElementById("submit").disabled = true;
            return false;
        }
    }


}