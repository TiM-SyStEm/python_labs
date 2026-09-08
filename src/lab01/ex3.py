price = 1000
discount = 10
vat = 20
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f"""
База после скидки: {base: .2f} ₽
НДС:               {vat_amount: .2f} ₽
Итого к оплате:    {total: .2f} ₽
"""
)