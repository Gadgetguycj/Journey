window.onload = function getName() {
    var name;
    var userData;
    
    $.ajax({
        "url": "http://journey.gadget.sh:8080/user",
        "method": "GET",
        "timeout": 0,
        "async": false,
        "headers": {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDE5NjE0MzYsInN1YiI6IjYxYjZiNzIxOTg4ODk0NTQ2ZDk1YmZmNyIsInRpZCI6IjEifQ.vO7NgkrxTs-Bzcwf8DLVfjVnWQt3O1umsl5UUgpTazs"
        },
        "success": function(data){
            name = data.fullname;
            console.log(name);
        }
    });
    
    firstname = name.split(" ")
    
    document.getElementById("usersName").innerHTML = firstname[0]
}
