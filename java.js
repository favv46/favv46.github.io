function onload() {
    if (navigator.userAgentData.mobile) {
        window.location.href = "Home.mobile.html"
    }
    else {
        window.location.href = "Home.html"
    }
    }