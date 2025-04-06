console.log('start');

setTimeout(() => {
    console.log('inside timeout');
}, 0);

async function wait() {
    console.log('inside wait');
    await new Promise(resolve => 
        setTimeout(() => console.log('inside promise'), 2000)
    );
    console.log('after wait');
}

wait();

console.log('end');