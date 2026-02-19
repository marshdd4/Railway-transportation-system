<<<<<<< HEAD
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
=======
def validate_card(card_number, cvv2, expiry, password):
    """
    اعتبارسنجی ساده کارت - برای تست پروژه
    هر کارتی با شماره ۱۶ رقمی، cvv2 چهار رقمی و تاریخ معتبر قبول می‌شود
    """
    if not (card_number and cvv2 and expiry and password):
        return False
    if not card_number.isdigit() or len(card_number) < 16:
        return False
    if not cvv2.isdigit() or len(cvv2) != 4:
        return False
    if '/' not in expiry or len(expiry.split('/')) != 2:
        return False
    # یک کارت خاص برای تست (اختیاری)
    if card_number == "1234567890123456" and cvv2 == "1234" and expiry == "12/25" and password == "1234":
        return True
    return True  # برای تست، همه کارت‌های با فرمت درست قبول شوند
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
