// Set interval to print "Hello" every 500 milliseconds
const interval = setInterval(printHello, 500);

let count = 0; // Variable to keep track of the number of times "Hello" is printed

// Function to print "Hello"
function printHello() {
  console.log("Hello");
  count++;

  // Check if "Hello" has been printed 10 times
  if (count === 10) {
    clearInterval(interval); // Clear the interval after printing 10 times
  }
}



// Set a timeout to stop the interval after 5000 milliseconds (10 times * 500 milliseconds)
setTimeout(() => {
  clearInterval(interval); // Clear the interval after 5000 milliseconds (10 times * 500 milliseconds)
  console.log("Printed exactly 10 times.");
}, 5000);
