window.onload = function getName() {
    var name;
    var userData;
    
    $.ajax({
        "url": "http://journey.gadget.sh:8080/user",
        "method": "GET",
        "timeout": 0,
        "async": false,
        "headers": {
        "Authorization": "Bearer " + localStorage.getItem("token")
        },
        "success": function(data){
            name = data.fullname;
            console.log(name);
        }
    });
    
    firstname = name.split(" ")
    firstname[0] = firstname[0[0]].toUpperCase();
    document.getElementById("usersName").innerHTML = firstname[0]
}
