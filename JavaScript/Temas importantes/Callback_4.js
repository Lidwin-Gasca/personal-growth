//💠This is now a CALLBACK🎈

function firstAction(callback){//estoy agregando un parametro
    console.log("I'm the first action");
    setTimeout(callback, 2000);
}

function secondAction(){
    console.log("I'm the second action");
}

setTimeout(() => firstAction(secondAction), 3000); // no solo seguimos usando el parametro pero lo converitmos en una funcion flecha



//we made it a Callback again. Ahora ya se puede considerar callback.
