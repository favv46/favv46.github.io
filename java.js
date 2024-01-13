function onload() {
    if (navigator.userAgentData.mobile) {
        window.location.href = "Home_mobile.html"
    }
    else {
        window.location.href = "Home.html"
    }
    }

/*
const buttons = document.getElementsByClassName("buttons")
for (let i = 0; i < buttons.length; i ++){
    buttons[i].addEventListener("mouseenter", function (){
        const h1 = buttons[i].querySelector("h1")
        if (h1){
            h1.style.fontFamily = "Integral_CF_Heavy"
            h1.style.fontSize = "1.07vw"
            h1.style.letterSpacing = "1px"
        }
    })
    buttons[i].addEventListener("mouseleave", function (){
        const h1 = buttons[i].querySelector("h1")
        if (h1){
            h1.style.fontFamily = "Snake"
            h1.style.fontSize = "3"
            h1.style.letterSpacing = "normal"
        }
    })
}
*/