let tg = window.Telegram.WebApp;
tg.expand();

let cart = [];

function addItem(name, price) {
    // Mahsulotni savatga qo'shish
    cart.push({ name: name, price: price });

    // Telegram Asosiy tugmasini yangilash
    tg.MainButton.text = `Savatda ${cart.length} ta mahsulot bor`;
    tg.MainButton.show();
}

// Telegram pastki tugmasi bosilganda ma'lumot yuborish
tg.onEvent('mainButtonClicked', function() {
    if (cart.length > 0) {
        let totalSum = cart.reduce((sum, item) => sum + item.price, 0);

        let data = {
            items: cart,
            total: totalSum
        };

        // Ma'lumotni JSON ko'rinishida bitta yuborish kifoya
        tg.sendData(JSON.stringify(data));
        tg.close();
    }
});
