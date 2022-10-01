// Object in JS resembles dict in Python and class object in Python
// in Python each class object has an underlying __dict__, so it's appropriate?

let testObj = {
    'hat': 'ballcap',
    'shirt': 'jersey',
    'shoes': 'cleast',
    'swimming suite': 'bra and panties'
}

// dot notation
console.log('testObj.hat: ' + testObj.hat);
// won't work with property key containing space: uncomment to check out
// console.log(testObj.swimming suite)

// bracket notation: if a property key contatins space, use this
// though it works anyway with any key
console.log("testObj['shirt']: " + testObj['shirt']);
console.log("testObj['swimming suite']: " + testObj['swimming suite']);

// update object property
testObj.hat = 'sombrero';
console.log('testObj.hat: ' + testObj.hat);

testObj['swimming suite'] = null;
console.log("testObj['swimming suite']: " + testObj['swimming suite']);

// we can add properties with both notations
testObj.pants = 'jeans';
testObj['jewels'] = 'earrings';

console.log('testObj.pants: '+ testObj.pants);
console.log('testObj.jewels: ' + testObj.jewels);

// delete a property
delete testObj.pants;
console.log('testObj.pants: ' + testObj.pants);

function checkProp(obj, prop) {
    if (obj.hasOwnProperty(prop)) {
        return obj[prop];
    } else {
        return 'not found';
    }
}

console.log(checkProp(testObj, 'hat'));
console.log(checkProp(testObj, 'dress'));

// nested objects work as nexted dicts in Python
// the same is true for nested arrays
