// window.addEventListener(window,"load", function() {
//     var loginForm = document.getElementById("LoginForm");
//     window.addEventListener(loginForm, "submit", function() {
//          login(loginForm);
//      });
//  });


function activateLogin(){
    const email = document.getElementById("emailID").value
    const password = document.getElementById("passwordID").value
    login(email, password)
    console.log("Logging in...")
}

function login(email, password){
    output = "" 
    console.log(email)
    console.log(password)
    var settings = {
        "url": "http://journey.gadget.sh:8080/user/login",
        "method": "POST",
        "timeout": 0,
        "async": false,
        "headers": {
        "Content-Type": "application/json"
        },
        "data": JSON.stringify({
        "email": email,
        "password": password
        }),
    };
    
    $.ajax(settings).done(function (response) {
        output = response
        localStorage.setItem("token", output.token) 
        window.location.replace("http://journey.gadget.sh/index.html");
    });

    return output
}
function logout(){
    localStorage.removeItem("token") 
    window.location.replace("http://journey.gadget.sh/login");
}

function activateCreation(){
    const name = document.getElementById("fullnameID").value
    const email = document.getElementById("emailID").value
    const weight = document.getElementById("weightID").value
    const height = document.getElementById("heightID").value
    const age = document.getElementById("ageID").value
    const password = document.getElementById("passwordID").value
    createAccount(name, email, weight, height, age, password)
    console.log("Logging in...")
}

function createAccount(name, email, weight, height, age, password){
    output = "" 
    console.log(email)
    console.log(password)
    var settings = {
        "url": "http://journey.gadget.sh:8080/user",
        "method": "POST",
        "timeout": 0,
        "async": false,
        "headers": {
        "Content-Type": "application/json"
        },
        "data": JSON.stringify({
        "fullname": name,
        "email": email,
        "weight": weight,
        "height": height,
        "age": age,
        "password": password
        }),
    };
    
    $.ajax(settings).done(function (response) {
        output = response
        window.location.replace("http://journey.gadget.sh/login.html");
    });

    return output
}
