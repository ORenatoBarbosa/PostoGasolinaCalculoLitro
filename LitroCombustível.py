litros = float(input('Digite a quantidade em litros: '))
combustivel = input('Digite o tipo de combustível A-álcool, G-gasolinaComum, C-GasolinaAditivada, D-Diesel: ').upper()

if combustivel == 'A':
    preco = litros * 1.9
    if litros <= 20:
        desconto = litros * ((preco * 3) / 100)
    else:
        desconto = litros * ((preco * 5) / 100)
    print('R$ %.2f' % (preco - desconto))

elif combustivel == 'G':
    preco = litros * 2.5
    if litros <= 20:
        desconto = litros * ((preco * 4) / 100)
    else:
        desconto = litros * ((preco * 6) / 100)
    print('R$ %.2f' %(preco - desconto))

elif combustivel == 'C':
    preco = litros * 3.5
    if litros <= 20:
        desconto = litros * ((preco * 5) / 100)
    else:
        desconto = litros * ((preco * 7) / 100)
    print('R$ %.2f' %(preco - desconto))
elif combustivel == 'D':
    preco = litros * 1.5
    if litros <= 20:
        desconto = litros * ((preco * 2) / 100)
    else:
        desconto = litros * ((preco * 4) / 100)
    print('R$ %.2f' %(preco - desconto))
else:
    print('Tipo inválido')

# Renato Barbosa
