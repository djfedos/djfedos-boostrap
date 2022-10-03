function trueOrFalse(isItTrue) {
    // note condition in parenthesis, unlike in Python 
    if (isItTrue) {
        return 'Yes, it\'s true';
    }
    return 'No, it\'s false';
}

function wasTrueOrFalse(wasItTrue) {
    if (wasItTrue) {
        return 'Yes, it\'s true';
    }
    else {
        return 'No, it\'s false';
    }
}

console.log(trueOrFalse(true));
console.log(trueOrFalse(false));
console.log(wasTrueOrFalse(true));
console.log(wasTrueOrFalse(false));

// 1 is truthy, 0 is falsy, familiar
console.log(trueOrFalse(1));
console.log(trueOrFalse(0));
console.log(wasTrueOrFalse(1));
console.log(wasTrueOrFalse(0));


// to assert equality use == operator (as in Python)
// this operator will try to convert types for comparison
// to avoid it use ===, it's a strict comparison operator

function testIfEqual(a, b) {
    if (a == b) {
        return 'Values are equal';
    }
    return 'Values are not equal';
}

console.log(testIfEqual(2, '2'));
console.log(testIfEqual(2.0, '2'));

function testIfStrictlyEqual(a, b) {
    if (a === b) {
        return 'Values are equal';
    }
    return 'Values are not equal';
}

console.log(testIfStrictlyEqual(2, '2'));
console.log(testIfStrictlyEqual(2.0, '2'));
console.log(testIfStrictlyEqual(2, 2));

// != works not like in Python but with type conversion

function testIfNotEqual(a, b) {
    if (a != b) {
        return 'Values not are equal';
    }
    return 'Values are equal';
}

console.log(testIfNotEqual(2, '2'));

// !== doesn't convert type

function testIfStrictlyNotEqual(a, b) {
    if (a !== b) {
        return 'Values are not equal';
    }
    return 'Values are equal';
}

console.log(testIfStrictlyNotEqual(2, '2'));
console.log(testIfStrictlyNotEqual(2.0, '2'));
console.log(testIfStrictlyNotEqual(2, 2));

// && instead of and keyword, || instead of or keyword
// else if, not elif - and it's not too useful as well

// !boolean turns boolean into its opposite
