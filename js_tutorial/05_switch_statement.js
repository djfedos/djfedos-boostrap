function caseInSwitch(val) {
    let answer;
    switch(val) {
        case 1:
            answer = 'alpha';
            break;
        case 2:
            answer = 'beta';
            break;
        case 3:
            answer = 'gamma';
            // try to comment out the next line and call function passing 3
            break;
        case 4:
            answer = 'delta';
            break;
        default:
            answer = 'omega';
            break;
    }
    return answer
}

console.log(caseInSwitch(5))

function caseMutlSwitch(val) {
    let answer;
    switch(val) {
        case 1:
        case 2:
        case 3:
            answer = 'alpha';
            break;
        case 4:
        case 5:
        case 6:
            answer = 'beta';
            break;
    }
    return answer
}

console.log(caseMutlSwitch(5))
    
