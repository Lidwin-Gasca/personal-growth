const userLeft = false;
const userWatchingCatMeme = false;

function watchTutorialPromise(){
    return new Promise((resolve, reject) => {
        if (userLeft) {
            reject({
                name: 'User Left',
                message: ':('
            })
        } else if (userWatchingCatMeme) {
            reject({
                name: 'User Watching Cat Meme',
                message: 'WebDevSimplified < Cat'
            })
        } else {
            resolve('thumbs up and Subcribe')
        }
    })
}

watchTutorialPromise().then((message) => {
    console.log('Succes: ' = message)
}).catch((error) => {
    console.log(error.name + ' ' + error.message)
})