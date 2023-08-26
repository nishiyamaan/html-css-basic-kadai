const abtn = document.getElementById("btn");

const changeText = () => {
    const getText = document.getElementById("text")
    getText.textContent = "ボタンをクリックしました"
}

abtn.addEventListener("click", () => {
    setTimeout(() => {
        changeText()
    }, 2000)
})

// これでいけてほしい
// abtn.addEventListener("click", setTimeout(changeText(), 2000))
