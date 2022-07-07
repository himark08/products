products=[]
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	#products.append([name, price])
	p = []
	p.append(name)
	p.append(price)

	products.append(p)
print(products)

print(products[0][0])
#用for loop存取清單
for p in products:
	print(p[0], '的價格是', p[1])