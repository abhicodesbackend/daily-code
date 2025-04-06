/**
 * Block scoping of variable with different declarations
 */

var string = 'JS';

function nameChange () {
    const string = 'javascript';
    console.log(string);
}

console.log(string);

nameChange();

console.log(string);