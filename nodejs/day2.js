/**
 * Comma operator (,) clubbed with IIFE (Immediate Invoked Function Expression)
 */

let a = 1;

let b = (a++, a++, a => a + 1)(a);

console.log(b);