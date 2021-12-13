window.onload = function addFoodToLog() {
  var table = document.getElementById("food_log");
  var dataStore;
    $.ajax({
        "url": "http://journey.gadget.sh:8080/food",
        "method": "GET",
        "timeout": 0,
        "async": false,
        "headers": {
        "Authorization": localStorage.getItem("token")
        },
        "success": function(data){
            dataStore = data;
            console.log(dataStore[0])
        }
    });
    
    for(const element of dataStore) {
        var row = table.insertRow(-1);
        var food = row.insertCell(0);
        var calories = row.insertCell(1);
        var carbs = row.insertCell(2);
        var fats =  row.insertCell(3);
        var proteins =  row.insertCell(4);
        var button = row.insertCell(5);
        
        food.innerHTML = element.name ;
        calories.innerHTML = element.total_calories + " Kcals";
        carbs.innerHTML = element.total_carbs + " g";
        fats.innerHTML = element.total_fat +" g";
        proteins.innerHTML = element.total_protein + " g";
        button.innerHTML = '<button onclick="add()">Add</button>';
    }
}

//function add(){
//        
//      var dataStore;
//    $.ajax({
//        "url": "http://journey.gadget.sh:8080/foodlog",
//        "method": "POST",
//        "timeout": 0,
//        "async": false,
//        "headers": {
//        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDE5NjE0MzYsInN1YiI6IjYxYjZiNzIxOTg4ODk0NTQ2ZDk1YmZmNyIsInRpZCI6IjEifQ.vO7NgkrxTs-Bzcwf8DLVfjVnWQt3O1umsl5UUgpTazs",
//        "Content-Type": "application/json"},
//        
//        "data": JSON.stringify({
//            
//        })
//        }
//    });
//}