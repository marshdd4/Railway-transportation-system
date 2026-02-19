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