function addFoodToLog() {
  var table = document.getElementById("food_log");
  var dataStore;
    $.ajax({
        "url": "http://journey.gadget.sh:8080/food",
        "method": "GET",
        "timeout": 0,
        "async": false,
        "headers": {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDE5NjE0MzYsInN1YiI6IjYxYjZiNzIxOTg4ODk0NTQ2ZDk1YmZmNyIsInRpZCI6IjEifQ.vO7NgkrxTs-Bzcwf8DLVfjVnWQt3O1umsl5UUgpTazs"
        },
        "success": function(data){
            dataStore = data;
            console.log(dataStore[0])
        }
    });
  
//  var row = table.insertRow(0);
//  var cell1 = row.insertCell(0);
//  var cell2 = row.insertCell(1);
//  cell1.innerHTML = "NEW CELL1";
//  cell2.innerHTML = "NEW CELL2";
    
    for(const element of dataStore) {
        var row = table.insertRow(0);
        var food = row.insertCell(0);
        var calories = row.insertCell(1);
        var carbs = row.insertCell(2);
        var fats =  row.insertCell(3);
        var proteins =  row.insertCell(4);
        
        food.innerHTML = element.name ;
        calories.innerHTML = element.total_calories + " Kcals";
        carbs.innerHTML = element.total_carbs + " g";
        fats.innerHTML = element.total_fat +" g";
        proteins.innerHTML = element.total_protein + " g";
    }
}

function deleteRow() {
  document.getElementById("food_log").deleteRow(0);
}