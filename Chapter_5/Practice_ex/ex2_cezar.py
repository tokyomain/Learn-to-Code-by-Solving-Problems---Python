# COCI '17 Contest 1 #1 Cezar
# https://dmoj.ca/problem/coci17c1p1


# input 1 : N (1 <= N <= 52) > number of cards Caesar has drawn so far.
# input 2 : 


# x > difference of 'sum of cards' to 21

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]*4
caesar_cards = []
greater = 0
smaller = 0

n = int(input())

for num in range(n):
    card = int(input())
    caesar_cards.append(card)

remaining_cards = 52 - len(caesar_cards)
sums = sum(caesar_cards)
x = 21 - sums

for c in caesar_cards:
    deck.remove(c)

for card in deck:
    if card > x:
        greater += 1
    else:
        smaller += 1


if greater >= smaller:
    print('DOSTA')
else:
    print('VUCI')

'''print(caesar_cards)
print(f'Total sum:{sums}')
print(f'X:{x}')
print(remaining_cards)
print(len(deck))
print(f'Greater: {greater}')
print(f'Smaller: {smaller}')'''