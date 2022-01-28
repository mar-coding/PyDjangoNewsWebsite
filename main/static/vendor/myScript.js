function hideObj(myid) {
    if (myid == "SigninForm"){
        document.getElementById(myid).style.display = "none";
        document.getElementById("SignupForm").style.display = "block";
    }else{
        document.getElementById(myid).style.display = "none";
        document.getElementById("SigninForm").style.display = "block";
    }
}