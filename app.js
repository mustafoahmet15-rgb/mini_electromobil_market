let tg = window.Telegram.WebApp;
tg.expand(); // Ilovani to'liq ekranga yoyish

let cart = [];

// Savatga mahsulot qo'shish funksiyasi
function addItem(name, price) {
    // Mahsulotni savatga qo'shamiz
    cart.push({ name: name, price: price });

    // "Main Button" (Telegramning pastki asosiy tugmasi) ni sozlash
    let mainBtn = tg.MainButton;
    mainBtn.text = `Savatda ${cart.length} ta mahsulot bor`;
    mainBtn.show(); // Tugmani ko'rsatish
}

// Telegram Main Button bosilganda (Buyurtma berish)
tg.onEvent('mainButtonClicked', function() {
    if (cart.length > 0) {
        // Jami summani hisoblash
        let totalSum = cart.reduce((sum, item) => sum + item.price, 0);

        // Botga yuboriladigan JSON ma'lumoti
        let data = {
            items: cart,
            total: totalSum
        };

        // Ma'lumotni yuborish va Web App'ni yopish
        tg.sendData(JSON.stringify(data));
        tg.close();
    } else {
        alert("Savat bo'sh!");
    }
});

// Agar siz HTML'da shaxsiy "main-btn" ID li tugma ishlatgan bo'lsangiz:
// (Bu qism ixtiyoriy, agar Telegram'ning o'z tugmasidan foydalansangiz yuqoridagisi kifoya)
document.getElementById("main-btn")?.addEventListener("click", function() {
    if (cart.length > 0) {
        let totalSum = cart.reduce((sum, item) => sum + item.price, 0);
        let data = {
            items: cart,
            total: totalSum
        };
        tg.sendData(JSON.stringify(data));
        tg.close();
    }
});
