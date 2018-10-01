USER = "KateLin"
PASS = "verysecurepassword123!"

def checkInfo(user,pswd):
    if(user != USER):
        return "Invalid Username"
        if(pswd != PASS):
            return "Invalid Password"
    return "Login successful"
