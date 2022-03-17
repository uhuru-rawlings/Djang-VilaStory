const removeError = (clicked_id) =>{
    
    document.getElementById(clicked_id).style.border = "none";
}

const ValidateSignin = () =>{
    let useremail = document.getElementById("useremail");
    let passwords = document.getElementById("userpassword");
    let rememberme = document.getElementById("rememberme");
    if(useremail.value.trim() === "" || passwords.value.trim() === ""){
        if(useremail.value.trim() === ""){
            useremail.style.border = "1px solid red";
            return false;
        }else{
            passwords.style.border = "1px solid red";
            return false;
        }
    }else{
        if(rememberme.checked){
            alert("checked")
            localStorage.setItem("useremail", useremail);
            localStorage.setItem("passwords", passwords);
        }
    }

}

const getcredentials = () =>{
    let userem = localStorage.getItem("useremail");
    let userpass = localStorage.getItem("passwords");
    document.getElementById("useremail").value = userem;
    document.getElementById("userpassword").value = userpass;
    
    setTimeout("getcredentials", 100);
}
window.onload = getcredentials;