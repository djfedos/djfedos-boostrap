var myGlobal = 10;

function fun1() {
    // without var keyword this var becomes global by mistake
    // put var keyword to make this var local
    oopsGlobal = 21;
}


function fun2() {
    var output = '';
    if (typeof(myGlobal) != undefined) {
        output = 'myGlobal :' + myGlobal;
    }
    if (typeof(oopsGlobal) != undefined) {
        output = 'oopsGlobal is global and it\'s value is: ' + oopsGlobal;
    }

    console.log(output);

}

fun1();
fun2();


function fun3() {
    var myLocal = 20;
    console.log(myLocal);
}

fun3();

// uncomment the next line to get Uncaught ReferenceError: myLocal is not defined
// console.log(myLocal)

function fun4() {
    var myGlobal = 144;
    return myGlobal;
}

console.log(fun4());
console.log(myGlobal);

// return keyword behaves pretty much like in Python in first approach

function nextInLine(arr, item) {
    arr.push(item);
    return arr.shift();
}

var testArr = [1, 2, 3, 4, 5];

console.log('Before: ' + JSON.stringify(testArr));
console.log(nextInLine(testArr, 6));
console.log('After: ' + JSON.stringify(testArr));

// var has functional scope
// let has block scope

// what is a block in JS? that's what it is

{   
    // anything enclosed in curly braces is a block
    // it could as well be a function, a for loop, a switch statement. neat! 
    let message = 'quick brown fox'
    console.log(message)
}

// everything that's not inside the curly braces is in the default block
// thus if you declare the variable with the same name twice in the same block,
// say in the default block, you get an error
let message = 'lazy dog'
console.log(message)

// let's try to play with fuction scope vs block scope

function hasBlockInIt(arr) {
    // var i = 'this was our array';
    let i = 'this was our array';
    
    for (el in arr) {
        // var i = el; 
        let i = el;
        console.log(i);
    }
    console.log(i);

}

hasBlockInIt([1, 2, 3, 4])

// if you'll uncomment variables with var you'll see that both are in
// the scope of a whole function, and i in for loop overrides the i from outside

// that's why using let to declare variables is preferrable
// it's kind of more intuitive, and allows to avoid hoisting (see below)
// const also has a block scope

// hoisting:

var x = function() {
    console.log(y)
    // console.log(z)
    var y = 'hoisted var'
    let z = 'non-hoisted let'
}

x()

// note that if you call y before assingment and (!) declaration, you get no errors
// the value of y is undefined though
// if you uncomment calling z before declaration and assignment, you'll get an error
// if it's necessary to use var and not let, expicitly declare and assign all vars
// on the top of the function (even if you use them later) to know what's going on


// see that the function below will once again output undefined
// it will use Windows object var only if we'll remove the func scope var

var yy = 'Window object var'

var xx = function() {
    console.log(yy)
    var yy = 'hoisted var'
}

xx()
