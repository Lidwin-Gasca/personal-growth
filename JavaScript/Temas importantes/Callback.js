//💠CALLBACK🎈

function firstAction(){
    console.log("I'm the first action");
}

function secondAction(){
    console.log("I'm the second action");
}

setTimeout(firstAction, 3000);
secondAction();