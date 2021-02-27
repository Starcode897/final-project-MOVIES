var test = d3.selectAll("li");
console.log(test);

var test2 = d3.select("#streammovie");
console.log(test2);

var test3 = test2.property("value");
console.log(test3);

var test4 = d3.select("li");
console.log(test4);

var test5 = test4.select("select");
console.log(test5);

//Iterate through each list item
test.forEach(function(list){
    console.log(list);
});
    //Save each property("value") to an object