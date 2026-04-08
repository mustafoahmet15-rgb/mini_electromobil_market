let tg = window.Telegram.WebApp;
tg.expand(); // Ilovani to'liq ekranga yoyish

let cart = [];

function addItem(name, price) {
    cart.push({ name: name, price: price });
    
    // Tugmani ko'rsatish va matnini yangilash
    let mainBtn = document.getElementById("main-btn");
    mainBtn.style.display = "block";
    mainBtn.innerText = Savatda `${cart.length} ta mahsulot bor`;
}

// "Savatni ko'rish" (main-btn) bosilganda
document.getElementById("main-btn").addEventListener("click", function() {
    if (cart.length > 0) {
        // Jami summani hisoblash
        let totalSum = cart.reduce((sum, item) => sum + item.price, 0);

        let data = {
            items: cart,
            total: totalSum
        };

        // app.js ichida
alert("Tugma bosildi, botga yuborilmoqda..."); 
tg.sendData(JSON.stringify(data));

        // Ma'lumotni botga yuborish
        tg.sendData(JSON.stringify(data)); 
        
        // Ilovani yopish
        tg.close();
    }
});
