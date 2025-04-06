/*
String to Integer (A to I)
Problem Description:
Convert a string s into an integer without using built-in functions

scenario 1: strings (lower, upper)
scenario 2: numbers (integer)
scenario 3: special chars can exist
scenario 4: combination of strings and integers, may include symbols as well
scenario 5: space
scenario 6: buffer/stream OR &, *

Different input cases:

"2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
abc2
abc200def
--1def
*/



function convert(str) {
  
    let result = 0, n = str.length, flag = false, isNegative = false;

    for (let i = 0; i < n; i++){
        
        if (str[i] == ' ') continue;
        if (str[i] == '-') {
        isNegative = true;
        continue;
        }
        
        let number = str[i] - '0';
        
        if (number >= 0 && number <= 9) {
        flag = true;
        result = result * 10 + number;
        } else {
        return flag ? result : 'NA';
        }
        
    }
    return isNegative ? result * -1 : result;
}

console.log(convert('   --25'));