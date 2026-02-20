# BANK.py - اعتبارسنجی کارت بانکی بر اساس قالب (بدون لیست ثابت)

import re
from datetime import datetime

def validate_card(card_number, cvv2, expiry, password):
    """
    اعتبارسنجی کارت بانکی با بررسی قالب فیلدها:
    - شماره کارت: دقیقاً ۱۶ رقم
    - cvv2: ۳ یا ۴ رقم
    - تاریخ انقضا: فرمت MM/YY و عدم انقضا
    - رمز: حداقل ۴ رقم
    """
    
    # 1. بررسی شماره کارت: باید ۱۶ رقم باشد
    if not re.fullmatch(r'\d{16}', card_number):
        print("Card number length must be 16 digits ❌")
        return False

    # 2. بررسی cvv2: باید ۳ یا ۴ رقم باشد
    if not re.fullmatch(r'\d{3,4}', cvv2):
        print("CVV2 must be 3 or 4 digits ❌")
        return False

    # 3. بررسی تاریخ انقضا
    #    قالب: MM/YY  (ماه دو رقمی، سال دو رقمی)
    if not re.fullmatch(r'(0[1-9]|1[0-2])/\d{2}', expiry):
        print("Exp date format must be MM/YY (e.g 12/25) ❌")
        return False

    try:
        exp_month, exp_year = map(int, expiry.split('/'))
        exp_year += 2000  # تبدیل 25 به 2025
        now = datetime.now()
        # بررسی عدم انقضا
        if exp_year < now.year or (exp_year == now.year and exp_month < now.month):
            print("Card is expired! ❌")
            return False
    except:
        # در صورت خطا در پردازش تاریخ، نامعتبر در نظر گرفته شود
        return False

    # 4. بررسی رمز کارت: حداقل ۴ رقم
    if not re.fullmatch(r'\d{4,}', password):
        print("Card password must be at least 4 digits. ❌")
        return False

    # اگر همه مراحل با موفقیت انجام شد، کارت معتبر است
    print("Card is Valid! ✅")
    return True