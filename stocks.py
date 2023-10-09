stockDict = {
    "GM": "General Motors",
    "CAT": "Caterpillar",
    "EK": "Eastman Kodak"
}

purchases = [
    ('GM', 100, '10-sep-2001', 48),
    ('CAT', 100, '1-apr-1999', 24),
    ('EK', 200, '1-jul-1998', 56)
]

total_income = 0

for purchase in purchases:
    company, shares, date, price = purchase
    print(f'{shares} shares at {price} dollars each on {date} from {company}')
    total_income = total_income + 100 * 48

print(f'Total value of stock in portfolio: {total_income}')

# 100 shares at 48 dollars each on 01-jul-1998
# 200 shares at 56 dollars each on 10-sep-2001

# Total value of stock in portfolio: $16000.
