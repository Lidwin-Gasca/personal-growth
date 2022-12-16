//💠This is not a CALLBACK🎈

function firstAction(callback){//estoy agregando un parametro
    console.log("I'm the first action");
    setTimeout(callback, 2000);
}

function secondAction(){
    console.log("I'm the second action");
}

setTimeout(firstAction(secondAction), 3000); // le agregue el parametro a la funcion "firstAction"
//                          ⬆
//                          |
// _________________________|____________________________
//|we opened up parenthesis so it's no longer a Callback.|
//'------------------------------------------------------'