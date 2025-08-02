name = "orange"
price_init = 0.8
good_num = 88088
growth_daily = 1.034
days = 13

a = round(price_init * (growth_daily ** days), 2)

print(f"商品编号{good_num} 商品名{name} 最终价格{price_init * (growth_daily ** days):.2f}")
print(a)