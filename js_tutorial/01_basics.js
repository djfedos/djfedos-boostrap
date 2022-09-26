/* Data types:
undefined, null, boolean, string, symbol, number, object
*/

var myName = "Teo";  // kind of global variable
console.log(myName);

myName = 8;

let courseName = "CodeCamp";  // kind of local variable
console.log(courseName);

const pi = 3.14;  // can't be changed later - immutable
console.log(pi);

// declaring a var - you can't simply do this in Python!
var a;
console.log('The a var is declared but not yet defined:');
console.log(a);

// declaring and assigning a var
var b = 2;

console.log(b);
console.log(myName);

// var++ and var-- work as in C to increment and decrement
b++;
console.log(b);

// var +=, -=, *=, /= work as in Python
b /= 2;
console.log(b);


// Escape chars like in Python
var myStr = "This is the so called \"String with a quote in it\" with escaped quotes";
console.log(myStr);
    
    
var secondStr = '<a href="https://djfedos.github.io" title="This lonk leads to my website">My homepage</a>'
console.log(secondStr);

// all the same with Python
var concatStr = myStr + secondStr;
console.log(concatStr);
var concatStrLen = 'String length = ' + concatStr.length;
console.log(concatStrLen);

// chars in string can be accessed by index like in Python

// strings are immutable, you can't change a char in a string, only the string as a whole

var helloStr = 'Jello world!'
helloStr[0] = 'H'
console.log(helloStr);
helloStr = 'Hello world!'
console.log(helloStr);
// one can't simply use -n index as in Python, it doesn't work here
console.log(helloStr[helloStr.length - 1]);

// Arrays can contain mixed data types, kind of like lists in Python
// Nested arrays are allowed
// Modification of arrays with access by index is allowed

var myArray = ['A', 10];
myArray[0] = 'E';
console.log(myArray);

// push() instead of append() method:

myArray.push('1355');
console.log(myArray);

// pop() method is the same
var myPop = myArray.pop();
console.log(myArray);
console.log(myPop);

myArray.push('1355');

// shift pops the first element and shifts the rest. convenient!
myPop = myArray.shift();
console.log(myArray);
console.log(myPop);

myArray.unshift('Y');
console.log(myArray);

// functions are like this: with and without args

function ourReusable() {
    console.log('Heyya World!');
}

ourReusable();
ourReusable();

function subtractNums(a, b) {
    console.log(a - b);
}

subtractNums(10, 5)
