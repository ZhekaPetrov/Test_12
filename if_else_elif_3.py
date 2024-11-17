print('Иду я такой в магазин')
bun = 50
pie = 84
money = int(input('Сколько у mеня с собой деньжат?'))
if bun <= money < pie:
    print('Я могу себе позволить только булочку')
if money >= pie and money < (bun * 2):
    print('В этот раз куплю себе пирожок!!!')
if money >= (bun * 2) and money < (pie * 2):
    print('Куплю ка я себе лучше 2 булочки')
if money >= (pie * 2):
    print('Сегодня жирую) Хватает аж на 2 пирожка!!!')
else:
    print('Может в следующий раз будут деньги...')
