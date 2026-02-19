# BANK.py - اعتبارسنجی واقعی کارت با لیست کارت‌های معتبر

# دیکشنری کارت‌های معتبر (شماره کارت به عنوان کلید)
# می‌توانید هر تعداد کارت که نیاز دارید به این لیست اضافه کنید
valid_cards = {
    "1234567890123456": {
        "cvv2": "1234",
        "expiry": "12/25",
        "password": "1234"
    },
    "1111222233334444": {
        "cvv2": "5678",
        "expiry": "11/24",
        "password": "4321"
    },
    # کارت‌های دیگری که می‌خواهید معتبر باشند
}

def validate_card(card_number, cvv2, expiry, password):
    """
    اعتبارسنجی کارت بانکی:
    - شماره کارت باید در لیست کارت‌های معتبر باشد
    - cvv2، تاریخ انقضا و رمز باید دقیقاً مطابق اطلاعات آن کارت باشد
    """
    # بررسی وجود کارت در لیست
    if card_number not in valid_cards:
        return False

    card_info = valid_cards[card_number]
    # بررسی تطابق cvv2، تاریخ و رمز
    if (card_info["cvv2"] == cvv2 and
        card_info["expiry"] == expiry and
        card_info["password"] == password):
        return True
    else:
        return False