const somthingWillHappen = () => {
    return new Promise((resolve, reject) => {
        if (true){ // esto lo puedo cambia a false, y el resultado sera'wooops'
            resolve('Hey');
        } else {
            reject('Whooooops');
        }
    });
};
somthingWillHappen()
    .then(response => console.log(response))
    .catch(err => console.error(err));



const somthingWillHappen2 = () => {
    return new Promise((resolve, reject) => {
        if (true){
            setTimeout(() => {
                resolve('True');
            }, 2000)
        } else {
            const error = new Error('Whooops');
            reject(error);
        }
    });
}
somthingWillHappen2()
    .then(response => console.log(response))
    .catch(err => console.error(err));


//usando el metodo .all()
Promise.all([somthingWillHappen(), somthingWillHappen2()])
    .then(response => {
        console.log('Array of results', response);
    })
    .catch(err => {
        console.error(err);
    })