let count = 0;

function cc(card) {
    switch(card) {
        case 2:
        case 3:
        case 3:
        case 4:
        case 5:
        case 6:
            count++;
            break;
        case 10:
        case 'J':
        case 'Q':
        case 'K':
        case 'A':
            count--;
            break;
    }

    let holdbet = 'hold'
    if (count > 0) {
        holdbet = 'bet'
    }
    return count + ': ' + holdbet
}

cc(2);
cc('Q');
cc(10);
cc('K');
cc('A');

console.log(cc(4));

