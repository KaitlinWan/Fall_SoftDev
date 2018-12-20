/*
Xiaojie(Aaron) Li, Kaitlin Wan
Softdev1 pd6
K29 -- Sequential Progression II: Electric Boogaloo
2018-12-18
*/

var studentList = ["ricky", "aaron", "kyle", "kaitlin", "tim", "bo", "damian", "michelle"];

// functions
var fib = function(args) {
    if (args == 0) return 0;
    else if (args == 1) return 1;
    else {
        return fib(args - 1) + fib(args - 2);
    }
}

var gcd = function(num, denom) {
    var temp = num % denom;
    if (temp == 0) return denom;
    else return gcd(denom, temp);
}


var randStudent = function() {
    var len = studentList.length;
    var rand = Math.floor(Math.random() * len);
    // console.log(rand);
    return studentList[rand];
}

// event listeners occur on click
var fibbo = document.getElementById("fib");
fibbo.addEventListener('click', function() {
    console.log("fib(10): " + fib(10));
    document.getElementById("fibr").innerHTML = "fib(10): " + fib(10);
});

var gcdo = document.getElementById("gcd");
gcdo.addEventListener('click', function() {
    console.log("gcd(30, 40): " + gcd(30, 40));
    document.getElementById("gcdr").innerHTML = "gcd(30, 40): " + gcd(30, 40);
});

var rando = document.getElementById("rand");
rando.addEventListener('click', function() {
    console.log("randStudent(): " + randStudent());
    document.getElementById("randr").innerHTML = "randStudent(): " + randStudent();
});
