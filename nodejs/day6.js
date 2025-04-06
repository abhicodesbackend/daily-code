console.log('start');

setTimeout(function() {console.log('timeout 1');}, 0);

Promise.resolve().then(() => console.log('promise 1'));

Promise.resolve().then(() => {console.log('promise 2');
                              setTimeout(function() {console.log('timeout 2');}, 0);});

console.log('end');