function validate(){
    var flag = true
    document.getElementById("mobile").className="form-control is-valid";
    
    if (/\d/.test(document.getElementById("fname").value)){
        document.getElementById("fname").className="form-control is-invalid";
        document.getElementById("fname-error").style.display = "block";
        flag = false;
    }
    else{
        document.getElementById("fname").className="form-control is-valid";
        document.getElementById("fname-error").style.display = "none";

    }
    if (/\d/.test(document.getElementById("lname").value)){
        document.getElementById("lname").className="form-control is-invalid";
        document.getElementById("lname-error").style.display = "block";
        flag = false;
    }
    else{
        document.getElementById("lname").className="form-control is-valid";
        document.getElementById("lname-error").style.display = "none";
    }

    if (document.getElementById("password").value !== document.getElementById("cpassword").value){
        document.getElementById("cpassword").className="form-control is-invalid";
        document.getElementById("confirm-error").style.display = "block";
        flag = false;
    }
    else{
        document.getElementById("cpassword").className="form-control is-valid";
        document.getElementById("confirm-error").style.display = "none";
    }

    return flag;
}   




document.getElementById("submit").addEventListener("click", (event) =>{
    if (!validate()){
        event.preventDefault();
        event.stopPropagation();
    }
})
