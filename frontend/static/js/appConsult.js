document.querySelector("#btnConsultUser").addEventListener("click", consult_user)

function consult_user(){
    var id = document.getElementById("id").value
    var obj = {
        "id": id,
    }
    sendData(obj)
}

function sendData(obj) {
    fetch("/consult_user", {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify(obj)
    })
    .then(response => response.json())
    .then(data => printData(data))
    
}

function printData(data){
    try {
        let fullname = data[0][0]
        let age = data[0][2]
        console.log(fullname)
        document.getElementById("name").value = fullname
        document.getElementById("age").value = age
    }
    catch {
        alert("El usuario no existe")
        clearBox()
    }    
}

function clearBox() {
    document.getElementById("id").value = ""
    document.getElementById("name").value = ""
    document.getElementById("age").value = ""
}
