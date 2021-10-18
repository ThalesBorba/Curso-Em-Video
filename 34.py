salary = int(input('Qual é o seu salário? '))
if salary < 1250:
    print('Você receberá um aumento de R${:.2f} e seu novo salário é R${:.2f}'.format(salary / 10, (salary / 10) + salary))
else:
    print('Você receberá um aumento de R${:.2f} e seu novo sálario é de R${:.2f}'.format(salary / 100 * 15, (salary / 100 * 15) + salary))
