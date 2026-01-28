import random

balance = 0
bet = 0

balance = int(input('Enter your starting balance: $'))
bet = int(input('Enter your bet amount(5$-10$-25$): $'))

while bet not in [5, 10, 25]:
    bet = int(input('Invalid bet amount. Please enter one of the three options 5$-10$-25$: $'))

while balance < bet:
   print(f'Insufficient balance. Yout current balance is: {balance}$')
   bet = int(input('Enter your bet amount(5$-10$-25$): $'))

while balance < 5:
   print('Insufficient balance to continue playing. Game over!')
   exit()

play_again = 'y'

while play_again.lower() == 'y' and balance >= bet:
    balance = balance - bet

    symbols = ['🍒','🍇', '🍉', '7️⃣']

    results = random.choices(symbols, k=3)

    print(f'{results[0]}  |  {results[1]}  |  {results[2]}')

    if results[0:3] == ['7️⃣', '7️⃣', '7️⃣']:
        balance = balance + bet * 10
        print(f'Jackpot! 💰 +{bet*10}$')
        print(f'Your new balance is: {balance}$')

    elif results[0:3] == ['🍉', '🍉', '🍉']:
        balance = balance + bet * 5
        print(f'Big Win! 💰 +{bet*5}$')
        print(f'Your new balance is: {balance}$')

    elif results[0:3] == ['🍇', '🍇', '🍇']:
        balance = balance + bet * 3
        print(f'Big Win! 💰 +{bet*3}$')
        print(f'Your new balance is: {balance}$')

    elif results[0:3] == ['🍒', '🍒', '🍒']:
        balance = balance + bet * 2
        print(f'Big Win! 💰 +{bet*2}$')
        print(f'Your new balance is: {balance}$')

    else:
        print('Try again!')
        print(f'Your new balance is: {balance}$')
    
    play_again = input('Do you want to play again? (Y/N): ')

    if balance < bet:
        print(f'Insufficient balance to continue playing with the current bet of {bet}$. Your current balance is: {balance}$')
        break

    if play_again.lower() == 'n':
        print(f'You are leaving the game with a balance of: {balance}$')
    
        
