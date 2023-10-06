//model
let images = [];
let input = [];
let i = 2;
let j = 2;
let a = 0;
let s = 0;

function push(userInput) {
    input.push(userInput);

}

function saveImage(response) { 
    images.push(response);
 }

 function iAnds(){
    i=i+1;
    s=s+1;
 }

 function jaAnds(){
    j = j + 1;
    a = j - 2;
    s = s - 1;
 }

//view
function render() {
    const display = document.getElementById('display');
    display.innerText = "";
    fetch(src).then((response) => {
        const img = document.createElement('img');
        img.setAttribute('src', response.url);
        display.appendChild(img);
        saveImage(response);
        
    });
   
}

function render1(x) {
    const display = document.getElementById('display');
    display.innerText = "";
    const img = document.createElement('img');
    img.setAttribute('src', (images[images.length - x]).url);
    display.appendChild(img);
}

// document.getElementById('download').style.width=window.innerWidth
//control
function download() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", images[s].url, true);
    xhr.responseType = "blob";
    xhr.onload = function () {
        var urlCreator = window.URL || window.webkitURL;
        var imageUrl = urlCreator.createObjectURL(this.response);
        var tag = document.createElement('a');
        tag.href = imageUrl;
        tag.download = input[input.length - 1];
        document.body.appendChild(tag);
        tag.click();
        document.body.removeChild(tag);
    }
    xhr.send();
}

function getImage() {
     let width = ""+window.innerWidth;
     let height = ""+window.innerHeight;
    const userInput = document.getElementById('input').value;
    input.push(userInput);
    src = "https://source.unsplash.com/random/"+width+"x"+height+"/?" + userInput + "=1"

    render();
    //animate these

    document.getElementById('loader').style.opacity =1
    document.getElementById('back').style.opacity =1
    document.getElementById('forward').style.opacity =1
    document.getElementById('download').style.opacity =1


    document.getElementById('input').value = ''

    
}

function forward() {
    let width = ""+window.innerWidth;
     let height = ""+window.innerHeight;
    const userInput = input[input.length - 1];

    src = "https://source.unsplash.com/random/"+width+"x"+height+"/?" + userInput + "=" + i;
    
    iAnds();

    if (a === 0) {
        render();
        j = 2;
    }

    else {

        render1(a);

        a = a - 1;

    }
    
}


function back() {
   
    render1(j);
   jaAnds();
}


document.body.addEventListener("keypress",()=>{
     // 75 is keycode of 'k'
    if(event.keyCode===13)
    {
        document.getElementById('getImage').click();
    }
   
    // console.log(event);
});
document.body.addEventListener("keydown",()=>{
    if(event.keyCode===39){
        document.getElementById('forward').click();
    }
    // console.log(event);
    
    if(event.keyCode===37){
        document.getElementById('back').click();
    }
    // console.log(event);
    if(event.keyCode===40){
        document.getElementById('download').click();
    }
});


let touchstartX = 0
let touchendX = 0
    
function checkDirection() {
  if (touchendX < touchstartX) {
    forward()
  }
  if (touchendX > touchstartX) {
    back()
  }
}

document.addEventListener('touchstart', e => {
  touchstartX = e.changedTouches[0].screenX
})

document.addEventListener('touchend', e => {
  touchendX = e.changedTouches[0].screenX
  checkDirection()
})