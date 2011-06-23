/**
 *  Testing the Radius Client Connection Pool
 */
var Radius = require("../lib/RADIUS.js");

//enable debugging
Radius.debug = true;

var client = new Radius.Client();

var callback = function(res, attr){ 
    console.log("RESPONSE RECEIVED"); 
    console.log(Radius.RESPONSE_CODES[res]);
    console.log(attr); 
};

console.log("ABOUT TO MAKE REQUEST!");
client.Auth({"user-name": "testuser", "password": "testpass", "service-type": "framed-user"}, callback);

// Closing the connecting ensure all requests finish!
console.log("CLOSING CLIENT CONNECTION");
client.Close();
