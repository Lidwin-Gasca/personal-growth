// we are going to set a new promise and this promise object is going to take one parameter which is a function which gets passed to variables of resolve and reject.
//so we have a resolve parameter and our reject parameter.

let p = new Promise((resolve, reject) => {  //And then we need to actually create the definition of that function inside.
    let a = 1 + 1;  //Inside of this promise section we need to find what the actual example the code inside of here would be me giving you the best video ever 
    //                of promises so we're just going to put some simple code here we're gonna create a variable "a" we're just going set it to 1 plus 1.
    if (a == 2){
        //so that way this is what the promise does and if this failed we would be reject it so would say if "a" is equal to 2 we would resolve it
        // but if it's not we would reject.
        resolve('success')
    } else {
        reject('failed') //so in the reject we gonna pass the message that said 'failed', and then in our resolve, this again we can pass it absolutly 
        //                  anything we want but we'll just pass it a message that says 'success' 
    }
//   so as you know this code is alweays gonna be successful because 1 plus 1 is always equal to two, so it's going to recall, this is resolve method that gets 
//   passed in.
});



//➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖



let p = new Promise((resolve, reject) => {  
//  let a = 1 + 1;  
    let a = 1 + 2;     //but if we change this to be 1 plus 2
                       //we would get the reject method because it doesn't equal two anymore an we would be calling the reject method.
    if (a == 2){
       
        resolve('success')
    } else {
        reject('failed'); //                                                                                      ➡ ➡ ➡ ➡ ➡ ➡ ➡   p.then  ⬅ ⬅ ⬅ ⬅ ⬅ ⬅ ⬅
    }//                                                                                                         ↗                                                  ↖
});//                                                                                                           ⬆                                                    ⬆
//     so now let's look at how we actually interact with promises so if we go down here we can just say that "p" since is a promise then all we have to do is say "." (it's an actual dot) then anything  inside of a dot then is gonna run for a resolve.



//todo lo que este en un ".then" sera automaticamente "resolve" resuelto, lo que pasa dentro de el "p.then" sera lo que sucede cuando la promesa se cumpla.

p.then((message) => {   //el parentesis despues del p.then es el 'method', no se como se llama, p.then() ⬅ese de ahi es el 'metodo' que se usa. apartir del metodo hacen la funcion flecha.
    console.log('this is in the then ' + message)  //la funcion flecha de equivale a esto   ➡     p.then(function (message) {console.log('this is in the then ' + message)});
}).catch((message) => {   
    console.log('this is in the then ' + message)  
});             // ".catch" lo que hace es capturar los errores, es decir los "reject", funciona como un especie de "else" y/o tambien como el "break" de los switches.

//esto de las promesas es similar a los callback, pero mas limpios.

    //REPASO:
    //.then         es llamado para un 'resolve' o sea cierto, correcto, completado
    //.catch        es llamado para un 'reject' o sea falso, fallido,  failed