let tg = window.Telegram.WebApp;
tg.expand(); // Ilovani to'liq ekranga yoyish

let cart = [];

function addItem(name, price) {
    cart.push({name, price});
    document.getElementById("main-btn").style.display = "block";
    document.getElementById("main-btn").innerText = `Savatda ${cart.length} ta mahsulot bor`;
}

// "Savatni ko'rish" bosilganda botga ma'lumot yuborish
document.getElementById("main-btn").addEventListener("click", function(){
    let data = {
        items: cart,
        total: cart.reduce((sum, item) => sum + item.price, 0)
    };
    tg.sendData(JSON.stringify(data)); // Ma'lumotni botga yuboradi
    tg.close(); // Ilovani yopadi
});