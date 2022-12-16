//💠CALLBACK🎈

function firstAction(callback, message, anotherCallback){//agregamos un tercer parametro
    console.log("I'm the first action");
    setTimeout(callback, 2000);
    anotherCallback();//anadimos esta linea de codigo para ejecutar la funcion "thirdAction"
}

function thirdAtion(){
    console.log("I'm the third action");
}

function secondAction(message){//                                      ________________________________________________________________________
    console.log(message);//                                           |    el tercer parametro que fue agregado en la primera linea de codigo  |
}//                                                                    ---------------------------------.--------------------------------------
//                                                                                                      ⬇ 
setTimeout(() => firstAction( () => secondAction("I'm the second action"), "I'm the first action", thirdAtion), 3000);// "anotherCallback" pasaria a llamarse "thirdAction"


//ahora lo que hicimos fue hacer la primera funcion reutilizable para imprimir un mensje y a la vez llamar la segunda funcion, que tambien sera reutilizable.

// hicimos lo mismo pero con la primera funcion tambien, ademas de agregar otro parametro 

//esto es esencialmente lo que sucede debajo de "setTimeout()" y tambien "addEventListener()"