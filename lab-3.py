import math
# Лабораторна робота №3
# Тема: Аналіз ризику та прийняття рішень в умовах невизначеності
capital = 100_000 

U = lambda x: 2 * math.sqrt(x)
x_a = capital * 1.15
U_a = U(x_a)
p1, p2 = 0.4, 0.6
x1, x2 = capital * 1.5, capital

EU_b = p1 * U(x1) + p2 * U(x2) 
CE_b = (EU_b / 2) ** 2

expected_value_b = p1 * x1 + p2 * x2
risk_premium = expected_value_b - CE_b

if EU_b > U_a:
    decision = "ризикове вкладення"
else:
    decision = "депозит"
    
print(f"U(депозит) = {U_a:.4f}")
print(f"Очікувана корисність (ризик) = {EU_b:.4f}")
print(f"Еквівалентна певність (CE) = {CE_b:.2f}")
print(f"Очікуване значення ризикової інвестиції = {expected_value_b:.2f}")
print(f"Премія за ризик = {risk_premium:.2f}")
print(f"Доцільніше обрати: {decision}")
