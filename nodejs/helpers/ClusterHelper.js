const cluster = require('cluster');
const numCPUs = require('os').cpus().length;

// Check if this is the master process
if (cluster.isPrimary) {
  console.log(`Master process ${process.pid} is running`);

  // Fork workers equal to CPU count
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  // Log when a worker exits
  cluster.on('exit', (worker, code, signal) => {
    console.log(`Worker ${worker.process.pid} died`);
  });
} else {
  // This code runs in worker processes
  console.log(`Hello from child process ${process.pid}`);
}