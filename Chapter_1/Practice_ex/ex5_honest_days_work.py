
# Input A : P > (1 <= P =< 100) > litres of the stuff
# Input B : B > (1 <= P =< 100) > litres of paint
# Input C : D > (1 <= P =< 100) > Pokedollars for each badge

# Remaining paint > 1 Pokedollar for litre

# How much money will James make for Team Rocket in total,
#  from his sales of badges and leftover paint? Hopefully 
# it'll be enough for at least a loaf of bread!

# Output : int > the amount of money which James will make
# (in Pokedollars)

litres_paint = int(input())
litres_badge = int(input())
pokedollars_badge = int(input())

badges = int(litres_paint / litres_badge)
print('---------Number of badges: ', badges)
value = int(badges * pokedollars_badge)
print('---------Value in Pokedollars: ', value)
reminder = litres_paint % litres_badge
print('---------Litres of paint remaining: ', reminder)
print('  ')

total = value + (reminder * 1)

print('TOTAL amount of Pokedollars earned: ', total)
print('*******************************************')
print('  ')
print('  ')