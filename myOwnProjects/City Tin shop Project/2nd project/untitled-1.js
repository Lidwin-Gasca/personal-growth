"use strict"

const wordCheck = ['test', 'jump', 'run'];
const wordList = ['jump', 'test', 'run', 'fun', 'test', 'run', 'space', 'moon', 'test'];

const countWords = function(words, compare, i) {
    let finalCount = words.map(function(word){
        return compare.reduce(function(acc, val){
            if (word.toLowerCase() === val.toLowerCase()) 
            acc[word]++;
            return acc;
        }, {[word]:0})
    });
    return finalCount;
};

console.log(countWords(wordCheck, wordList));
console.log(countWords.length);
if (countWords.length !== 3) {
    //do nothing
}
else {
    console.log("show Picture");
}