/**
 * Identify blocked event loop
 */

// runs at every 2 seconds interval
setInterval(() => {
    const now = Date.now();
    if (now - last_checked > 2500) {
        console.warn('⚠️ Event loop blocked!', `for ${now - last_checked} ms`);
    } else {
        console.info('Event loop unblocked . . .');
    }
    last_checked = Date.now();
}, 2000);

let last_checked = Date.now();

// function sleep(ms) {
//     return new Promise(resolve => setTimeout(resolve, ms));
// }

// async function main(ms) {
//     await sleep(ms);
//     console.log(`Event loop was on sleep for ${ms} milliseconds`);
// }

// main(5000);

function block(ms) {
    const start = Date.now();
    while (Date.now() - start < ms) {
        // This blocks the event loop
    }
}

setInterval(() => block(5000), 5000);

