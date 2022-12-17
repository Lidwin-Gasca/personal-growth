
// Next create a JavaScript file named script.js and include our code.

// Let’s start with getting a reference to html canvas tag using Document.getElementbyId() , element’s context using HTMLCanvasElement.getContext() and defining the block that will move in the canvas.

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

var block={
    x:185,
    y:185,
    side:30,
    color:"purple",
    drawBlock: function(){ 
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x,this.y,this.side,this.side);}
}




// After completing HTML, CSS, and adding some JavaScript our application will look like this but wait, it is not performing any function yet so, let’s add some.
// Now comes the time to add Speech Recognition functionality into our application.
// First, we need to add Chrome Support to our application.
// Support for Web Speech API speech recognition is currently limited to Chrome for Desktop and Android — Chrome has supported it since around version 33, but with prefixed interfaces, so we need to include prefixed versions as shown in the code below.
var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition
var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList
var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent



// Next, we will define the grammar we want our app to recognize. It is the four directions(right, left, up, down) in our case. The following variable is defined to hold our grammar.
var directions = [ 'up', 'down','left','right'];
var grammar = '#JSGF V1.0; grammar directions; public <direction> = ' + directions.join(' | ') + ' ;'



// The next thing to do is define a speech recognition instance to control the recognition for our application. This is done using the SpeechRecognition() constructor. We also create a new speech grammar list, a list of words or patterns of words that we want the recognition service to recognize to contain our grammar, using the SpeechGrammerList() constructor and defining other values.
var recognition = new SpeechRecognition();
var speechRecognitionList = new SpeechGrammarList();
speechRecognitionList.addFromString(grammar, 1);
recognition.grammars = speechRecognitionList;
recognition.continuous = false;
recognition.lang = 'en-US';
recognition.interimResults = false;
recognition.maxAlternatives = 1;


// Now get a reference to output <div> to display the diagnostic message and implement an onclick handler to start the speech recognition service whenever the screen is tapped/clicked. This is achieved by calling SpeechRecognition.start() method.
var diagnostic = document.querySelector('.output');

document.body.onclick = function() {
  recognition.start();
}



// Now, let’s add some event handlers by assigning an event listener to the oneventname property of this interface.

// onresult is fired when the speech recognition service returns a result — a word or phrase has been positively recognized
// onerror handles cases where there is an actual error with the recognition successfully
// onnomatch fired when the speech recognition service returns a final result with no significant recognition.
// onspeechend is fired when speech recognized by the speech recognition service has stopped being detected used to stop the speech recognition service from running using SpeechRecognition.stop() method.
recognition.onresult = function(event) {
    var direction = event.results[0][0].transcript;
    diagnostic.textContent = 'Result received: ' + direction + '.';
    moveBlock(direction)
}

recognition.onspeechend = function() {
    recognition.stop();
}
  
recognition.onnomatch = function(event) {
    diagnostic.textContent = "I didn't recognise that direction(up,down,right,left).";
}
  
recognition.onerror = function(event) {
    diagnostic.textContent = 'Error occurred in recognition: ' + event.error;
}


// Let’s add a moveBlock function with the help of which the block will move right, left, up, or down in the canvas. Here we have added constraints to ensure the block does not move out of the canvas.
function moveBlock(direction) {
    if(direction == 'right' && block.x<=360){ 
        block.x += 30; 
    }
    else if(direction == 'left' && block.x>30){
        block.x += -30; 
    }
    else if(direction == 'up' && block.y>30) {
        block.y += -30;
    }
    else if(direction == 'down' && block.y<=360){
        block.y += 30; 
    }
}


// Finally, let’s update the screen using requestAnimationFrame to show the movement of the block.

function update(){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    block.drawBlock();    
    requestAnimationFrame(update);
}
requestAnimationFrame(update);


// Conclusion

// We have discussed some of the properties, methods, and events of speech recognition so far. I hope this article gave you a basic understanding of Web Speech API. However, this is just an introduction, and there’s still a lot more. Feel free to explore…

// Happy Learning!