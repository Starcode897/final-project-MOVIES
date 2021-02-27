/*var test = d3.selectAll("li");
console.log(test);

var test2 = d3.select("#streammovie");
console.log(test2);

var test3 = test2.property("value");
console.log(test3);

var test4 = d3.select("li");
console.log(test4);

var test5 = test4.select("select");
console.log(test5);*/

//Iterate through each list item

    //Save each property("value") to an object

// if I cant get the loop
// jsut do it manually as it is a set value of properties
var gender = d3.select("#gender").property("value");
var retired = d3.select("#retired").property("value");
var partner = d3.select("#partner").property("value");
var dependents = d3.select("#dependents").property("value");
var tenure = d3.select("#tenure").property("value");
var telephone = d3.select("#telephone").property("value");
var lines = d3.select("#lines").property("values");
var internet = d3.select("#internet").property("values");
var security = d3.select("#security").property("values");
var backup = d3.select("#backup").property("value");
var protection = d3.select("#protection").property("value");
var techsupport = d3.select("#techsupport").property("value");
var streamtv = d3.select("#streamtv").property("value");
var streammovie = d3.select("#streammovie").property("value");
var contract = d3.select("#contract").property("value");
var billing = d3.select("#billing").property("value");
var method = d3.select("#method").property("value");
var currentpayment = d3.select("#currentpayment").property("value");

// save the values as individual cases
// will see if individual values or object works best
