/**
 * Asynchronous logging helper
 */


const logs = [];

// print all the available event loop logs in intervals of 5 seconds
setInterval(() => {
    if (logs.length) {
        console.log(logs.join('\n'));
        logs.length = 0;
    } else console.log('No logs to print . . .');
}, 5000);

let count = 1;

function log(msg) {
    logs.push(`${new Date().toISOString()} - ${msg}`);
}

setInterval(() => {
    let i = 0;
    while (i < 5) {
        log(count);
        i++;
        count++;
    }
}, 5000);