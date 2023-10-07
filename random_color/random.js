const btnEl = document.getElementById("btn");
const clrEl = document.getElementById("clrcode");
const containerEl = document.querySelector(".container");
const str = "0123456789abcdef";
const codelen = 6;

console.log(1)
function randomColor(){
    
    let code = "#";


    for (let i = 0; i < codelen; i++) {
        
        let j = Math.floor(Math.random()*str.length);
        code += str.charAt(j);
        console.log(code);

        
    }
    return code;
}

btnEl.addEventListener("click", function(){
    let color = randomColor();
    clrEl.innerText = color;

    containerEl.style.setProperty("--color",color)

})
