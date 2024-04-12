document.querySelector("#btnRegisterUser").addEventListener("click", register_user)

function register_user () {     
    var name  = document.getElementById("name").value
    var id = document.getElementById("id").value
    var age = document.getElementById("age").value
    var obj = {
        "name": name,
        "id": id,
        "age": age
    }
    sendData(obj)
}

function sendData(obj) {
    fetch("/register_user", {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify(obj)
    })
    .then(response => response.json())
    .then(data => clearBox(data))
}

function clearBox(data){
    if (data.message == "ok"){
        alert("User registered")
        document.getElementById("name").value = ""
        document.getElementById("id").value = ""
        document.getElementById("age").value = ""
    }
    else {
        alert("Error with the data")
    }
    
}