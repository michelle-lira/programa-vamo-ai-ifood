# Peça para a pessoa usuária inserir o nome de três produtos de mercado e seus respectivos
# preços;
# Mostre na tela o produto mais barato.

print("ME AJUDA A ECONOMIZAR NAS COMPRAS?")
print("Preciso que me sugira três produtos. Digite qual o item e o valor:")

produto1_nome = input("Qual o primeiro produto? ")
produto1_preco = float(input("Qual o preço?   R$ "))

produto2_nome = input("Qual o segundo produto? ")
produto2_preco = float(input("Qual o preço?   R$ "))

produto3_nome = input("Qual o terceiro produto? ")
produto3_preco = float(input("Qual o preço?   R$ "))

if produto1_preco < produto2_preco and produto2_preco < produto3_preco:
    print(f"{produto1_nome} é o item mais barato. Valeu pelas dicas!")
elif produto2_preco < produto1_preco and produto1_preco < produto3_preco:
    print(f"{produto2_nome} é o item mais barato. Valeu pelas dicas!")
elif produto3_preco < produto1_preco and produto1_preco < produto2_preco:
    print(f"{produto3_nome} é o item mais barato. Valeu pelas dicas!")

print()
print("BOAS COMPRAS!")
print()
