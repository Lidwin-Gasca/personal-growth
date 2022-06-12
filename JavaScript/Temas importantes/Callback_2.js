//💠CALLBACK🎈

function firstAction(){
    console.log("I'm the first action");
    setTimeout(secondAction, 2000);
}

function secondAction(){
    console.log("I'm the second action");
}

setTimeout(firstAction, 3000);

//1st argument is a Callback.