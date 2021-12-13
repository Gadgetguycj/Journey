window.onload = function getName() {
    var name;
    var calories;
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
            name = data;
            console.log(data);
        }
    });
    
       $.ajax({
        "url": "http://journey.gadget.sh:8080/user/calories",
        "method": "GET",
        "timeout": 0,
        "async": false,
        "headers": {
        "Authorization": "Bearer " + localStorage.getItem("token")
        },
        "success": function(data){
            calories = data;
            console.log(data);
        }
    });
    
    firstname = name.fullname.split(" ");
    
    document.getElementById("usersName").innerHTML = firstname[0];
}
