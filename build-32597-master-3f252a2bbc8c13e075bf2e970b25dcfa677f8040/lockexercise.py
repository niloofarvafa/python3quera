# دریافت ورودی‌ها
k = int(input())  # تعداد قفل‌های چرخان
code = input().strip()  # رمز مورد نظر

# بررسی اینکه رمز فقط شامل اعداد بین ۱ تا ۹ باشد
if not (len(code) == k and all(c in '123456789' for c in code)):
    raise ValueError("رمز باید دقیقا شامل اعداد بین ۱ تا ۹ باشد.")

total_turns = 0  # مجموع حداقل چرخش‌ها

# پردازش هر قفل
for i in range(k):
    lock = input().strip()  # ترتیب اعداد روی قفل
    
    # بررسی اینکه قفل باید دقیقا ۹ رقم باشد و شامل اعداد بین ۱ تا ۹
    if not (len(lock) == 9 and all(c in '123456789' for c in lock)):
        raise ValueError("ترتیب قفل باید دقیقا شامل ۹ رقم بین ۱ تا ۹ باشد.")
    
    current_digit = lock[0]  # عددی که نشانگر به آن اشاره می‌کند
    target_digit = code[i]  # عددی که باید به آن برسیم
    
    # موقعیت فعلی و موقعیت هدف در قفل را پیدا می‌کنیم
    current_pos = lock.index(current_digit)
    target_pos = lock.index(target_digit)
    
    # محاسبه چرخش در جهت ساعت‌گرد و پادساعت‌گرد
    clockwise_turns = (target_pos - current_pos) % 9
    counter_clockwise_turns = (current_pos - target_pos) % 9
    
    # اضافه کردن حداقل چرخش به مجموع
    total_turns += min(clockwise_turns, counter_clockwise_turns)

# خروجی مجموع حداقل چرخش‌ها
print(total_turns)
