import random

class Hand:
    def __init__(self):
        self.holding = []

    def get_total(self):
        total = 0
        for card_obj in self.holding:
            total += card_obj.real_value
        return total

class Player:
    def __init__(self):
        self.hand = Hand()  

    def show_hand(self, stand=False):
        if isinstance(self, Dealer):
            if not stand:
                print(f'Dealer --> {self.hand.holding[0]}')
            else:
                print(
                    f'Dealer --> {self.hand.holding} [{self.hand.get_total()}]')
        else:
            print(f'Human --> {self.hand.holding} [{self.hand.get_total()}]')

    def game_over(self, winner, done=False):
        print(f'{type(self).__name__} BUST')
        print(f'{type(winner).__name__} Wins')
        input('Press any key continue')


class Dealer(Player):
    def deal(self, recipient, card_deck):
        if len(recipient.hand.holding) >= 2:
            recipient.hand.holding.append(card_deck.cards.pop())
        else:
            for i in range(2):
                recipient.hand.holding.append(card_deck.cards.pop())


class Card:
    def __init__(self, suit, rank, face=False, ace=False):
        self.suit = suit
        self.rank = rank
        if ace:
            self.real_value = 1
        elif face:
            self.real_value = 10
        else:
            self.real_value = self.rank

    def __repr__(self):
        return f'<Card: [{self.suit} {self.rank}]>'


class Deck:
    def __init__(self):
        self.ranks = range(1, 14)
        self.suits = ['Club', 'Spade', 'Diamond', 'Heart']
        self.cards = self.build_deck()

    def build_deck(self):
        deck_list = []
        for s in self.suits:
            for r in self.ranks:
                if r == 1:
                    card = Card(s, 'A', ace=True)
                elif r == 11:
                    card = Card(s, 'J', face=True)
                elif r == 12:
                    card = Card(s, 'Q', face=True)
                elif r == 13:
                    card = Card(s, 'K', face=True)
                else:
                    card = Card(s, r)
                deck_list.append(card)
        return deck_list

    def shuffle_cards(self):
        print("Shuffling deck...")
        random.shuffle(self.cards)
        print("Deck shuffled...")


class Blackjack():
    current_round = 0

    @classmethod
    def run(cls):
        game_over = False
        while not game_over:

            deck = Deck()
            human = Player()
            dealer = Dealer()

            deck.shuffle_cards()

            confirm = input(
                "Press any key to continue. Type 'quit' to exit program. ").lower()
            if confirm == 'quit':
                game_over = True
            else:
                dealer.deal(human, deck)
                dealer.deal(dealer, deck)

                done = False

                cls.current_round = 1

                while not done:

                    if human.hand.get_total() == 21 and cls.current_round == 1:
                        print("Blackjack!")
                        print("Human wins")
                        print('Dealer loses')
                        break

                    elif human.hand.get_total() > 21 and cls.current_round == 1:
                        input('Invalid game. Press any key to try again.')
                        break
                    elif human.hand.get_total() > 21 and cls.current_round != 1:
                        human.game_over(dealer, done=True)
                        break
                    elif dealer.hand.get_total() > 21 and cls.current_round != 1:
                        dealer.game_over(human, done=True)
                        break

                    dealer.show_hand()
                    human.show_hand()

                    ask = input(
                        "Would you like to hit or stand? Type 'quit' to stop playing. ").lower()
                    if ask == 'quit':
                        done = True
                    elif ask == 'hit':
                        dealer.deal(human, deck)
                    elif ask == 'stand':
                        while dealer.hand.get_total() < 18:
                            
                            dealer.deal(dealer, deck)
                            human.show_hand()
                            dealer.show_hand(stand=True)
                        if dealer.hand.get_total() > 21:
                            dealer.game_over(human, done=True)
                        elif human.hand.get_total() > dealer.hand.get_total():
                            dealer.game_over(human, done=True)
                        elif human.hand.get_total() < dealer.hand.get_total():
                            human.game_over(dealer, done=True)
                        elif human.hand.get_total() == dealer.hand.get_total():
                            input(
                                'PUSH. The game is void. Press any key to continue.')
                            break
                        done = True
                    cls.current_round += 1


# blackjack = Blackjack()
# blackjack.run()
