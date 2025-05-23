/**
 * Function bindings and implicit calls
 */

var length = 4;

function callback() {
    console.log(this.length);
}

const object = {
    length: 5,
    method: function() {
        arguments[0]();
    }
}

object.method(callback, 2, 3);