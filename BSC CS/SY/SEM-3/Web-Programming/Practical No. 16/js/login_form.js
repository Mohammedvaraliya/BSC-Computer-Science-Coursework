let attempt = 3;

function validate() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    let passwordChecking = /^[a-zA-Z0-9!@#$%^&*]{4, 8}$/;
    if (passwordChecking.test(password) && username != "") {
        alert("Login successfully");
    }

    else {
        attempt--;
        alert("You have left " + attempt + " attempt;");
        
        if (attempt == 0) {
            document.getElementById("username").disabled = true;
            document.getElementById("password").disabled = true;
            document.getElementById("submit").disabled = true;
            return false;
        }
    }
}