var Client = require('node-rest-client').Client;
var client = new Client();

// direct way
client.get("localhost:5000/auth", function (data, response) {
    // parsed response body as js object
    console.log(data);
    // raw response
    console.log(response);
});
