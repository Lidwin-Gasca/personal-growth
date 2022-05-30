//💠CALLBACK🎈

function firstAction(callback){//estoy agregando un parametro
    console.log("I'm the first action");
    setTimeout(callback, 2000);
}

function secondAction(message){
    console.log(message);
}

setTimeout(() => firstAction( () => secondAction("I'm the second action")), 3000);


//ahora lo que hicimos fue hacer la primera funcion reutilizable para imprimir un mensje y a la vez llamar la segunda funcion, que tambien sera reutilizable.