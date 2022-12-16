
const doSomthingAsync = () =>{
    return new Promise((resolve, reject) => {
        (true)
        ? setTimeout(() => resolve('Do Somthing Async'), 3000)
        : reject(new Error('Test Error'))
    });
}
const doSomthing = async () => {
    const somthing = await doSomthingAsync();
    console.log(somthing);
}
console.log('Before');
doSomthing();
console.log('After');


const anotherFunction = async () => {
    try{
        const somthing = await doSomthingAsync();
        console.log(somthing);
    } catch (error) {
        console.error(error)
    }
}
console.log('Before-1');
anotherFunction();
console.log('After-1');

