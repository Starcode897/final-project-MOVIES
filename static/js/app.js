// Initialize the button instance
var button = d3.select("#filter-btn");

// Initialize the form instance
var form = d3.select("#form");

// Create Event handlers
button.on("click", runEvent);
form.on("submit", runEvent);

// Creates the output area to display monthly charges
function createOutput(){

    // Output results as an alert
    window.alert("test");
    var testOutput = document.getElementById("output");
    testOutput.value = "test";
    console.log(testOutput);
};

// function to listen to event and read in values
function runEvent(){

    // Prevent Page from Refreshing
    d3.event.preventDefault();

    // Declare a an object to save each value in survey
    var objTest = {};

    // Save values into the object
    objTest.gender = d3.select("#gender").property("value");
    objTest.retired = d3.select("#retired").property("value");
    objTest.partner = d3.select("#partner").property("value");
    //var dependents = d3.select("#dependents").property("value");
    objTest.tenure = d3.select("#tenure").property("value");
    objTest.telephone = d3.select("#telephone").property("value");
    objTest.lines = d3.select("#lines").property("values");
    objTest.internet = d3.select("#internet").property("values");
    objTest.security = d3.select("#security").property("values");
    objTest.backup = d3.select("#backup").property("value");
    objTest.protection = d3.select("#protection").property("value");
    objTest.techsupport = d3.select("#techsupport").property("value");
    objTest.streamtv = d3.select("#streamtv").property("value");
    objTest.streammovie = d3.select("#streammovie").property("value");
    objTest.contract = d3.select("#contract").property("value");
    objTest.billing = d3.select("#billing").property("value");
    objTest.method = d3.select("#method").property("value");
    objTest.currentpayment = d3.select("#currentpayment").property("value");

    console.log(objTest);

    // Call the create Output function
    createOutput(objTest);
}
