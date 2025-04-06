/**
 * Singleton Function
 */
 
function singleton() {
    let instance;
    let count = 0;
    
    function createInstance() {
      console.log('new instance created');
      return {'count': count};
    }
    
    return {getInstance: function () {
      if (instance) {
        console.log('existing instance');
        return instance;
      } else {
        instance = createInstance();
        return instance;
      }
    },
    increment: function() {
      return ++count;
    }
    };
  }
  
  let single = singleton();
  
  let one = single.getInstance();
  console.log(one);
  console.log(single.increment());
  let two = single.getInstance();
  console.log(two);
  console.log(single.increment());