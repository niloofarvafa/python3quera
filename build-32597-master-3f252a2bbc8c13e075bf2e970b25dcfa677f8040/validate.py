import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    pattern = r'^09\d{9}$'
    return bool(re.match(pattern, phone))

# تست ایمیل‌ها
print(validate_email("test@example.com"))  # True
print(validate_email("invalid-email@com"))  # False

# تست شماره موبایل‌ها
print(validate_phone("09123456789"))  # True
print(validate_phone("1234567890"))   # False
