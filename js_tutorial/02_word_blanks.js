// madlib

function wordBlanks(myNoun, myAdj, myVerb, myAdveb) {
    // could be one line, not two
    var result = ''
    result = 'The ' + myAdj + ' ' + myNoun + ' ' + myVerb + ' to the store ' + myAdveb + '.'

    return result
}

console.log(wordBlanks('dog', 'big', 'ran', 'quickly'))
console.log(wordBlanks('fox', 'quick', 'jumps', 'over the lazy dog'))
