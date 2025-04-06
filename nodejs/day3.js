/**
 * Singleton Classes
 */

class singleton
{
  constructor() {
    if (singleton.instance) {
      console.log('using existing instance');
      return singleton.instance;
    }
    console.log('creating new instance');
    singleton.instance = this;
    this.count = 0;
    return singleton.instance;
  }
  
  increment() {
    ++this.count;
    console.log(this.count);
  }
}

let one = new singleton();
one.increment();
let two = new singleton();
two.increment();
let three = new singleton();
three.increment();
three.increment();
three.increment();