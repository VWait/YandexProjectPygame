from random import shuffle


class Card:
    def __init__(self, game, value):
        self.game = game
        self.value = value

    def move(self):
        pass


class Card1(Card):
    def move(self):
        selected_player_i = self.game.choice_other_player(self.game.count_players, self.game.player_i)
        selected_card = self.game.choice_card_value()
        if self.game.players[selected_player_i].card.value == selected_card:
            print(f'Player {selected_player_i + 1} lose')
            del self.game.players[selected_player_i]
            self.game.count_players -= 1


class Card2(Card):
    pass


class Card3(Card):
    def move(self):
        selected_player_i = self.game.choice_other_player(self.game.count_players, self.game.player_i)
        if self.game.players[selected_player_i].card.value <= self.game.players[self.game.player_i].card.value:
            losing_player = selected_player_i
        elif self.game.players[selected_player_i].card.value >= self.game.players[self.game.player_i].card.value:
            losing_player = self.game.player_i
        else:
            return
        print(f'Player {losing_player + 1} lose')
        del self.game.players[losing_player]
        self.game.count_players -= 1


class Card4(Card):
    def move(self):
        # изменения в строчках 84, 87, 92, 96, 101
        self.game.players_activity[self.game.player_i] = False


class Card5(Card):
    def move(self):
        selected_player_i = self.game.choice_player(self.game.count_players)
        self.game.players[selected_player_i].card.value = self.game.deck.get_and_pop_card()


class Card6(Card):
    def move(self):
        selected_player_i = self.game.choice_other_player(self.game.count_players, self.game.player_i)
        free_player = self.game.players[selected_player_i].card.value
        self.game.players[selected_player_i].card.value = self.game.players[self.game.player_i].card.value
        self.game.players[self.game.player_i].card.value = free_player


class Card7(Card):
    def move(self):
        # изменения в 136-148 строчках
        return


class Card8(Card):
    def move(self):
        print(f'Player {self.game.player_i + 1} lose')
        del self.game.players[self.game.player_i]
        self.game.count_players -= 1



class Game:
    values_cards = {1: Card1, 2: Card2, 3: Card3, 4: Card4,
                    5: Card5, 6: Card6, 7: Card7, 8: Card8}

    def __init__(self):
        self.deck = Deck(self, [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8])
        self.count_players = 3
        self.players = [Player(self.deck.get_and_pop_card()) for i in range(self.count_players)]
        self.player_i = 0
        self.players_activity = [True for i in range(self.count_players)]

    def game_cycle(self):
        activity = self.players_activity
        while len(self.deck.deck) > 0:
            print([p.card.value for p in self.players])
            self.players[self.player_i].move(self.deck)
            self.player_i = (self.player_i + 1) % self.count_players
            self.players_activity = activity

    def choice_player(self, cnt_ps):
        """return player number"""
        return int(input('Pick one player: ' + ' '.join([str(i) for i in range(1, cnt_ps + 1)\
                                                         if self.players_activity[p_i] is True]))) - 1

    def choice_other_player(self, cnt_ps, p_i):
        """return player number"""
        return int(input('Pick one player: ' + ' '.join([str(i) for i in range(1, cnt_ps + 1)\
                                                         if i - 1 != p_i if self.players_activity[p_i] is True]))) - 1

    def choice_card_value(self):
        """return card number"""
        return int(input('Pick one card: ' + ' '.join([str(i) for i in range(2, 9)])))


class Deck:
    def __init__(self, game, cards):
        self.game = game
        self.values_cards = self.game.values_cards
        self.cards = cards
        self.deck = []
        self.fill_and_shuffle_deck()

    def save_card(self, value):
        self.deck.append(self.values_cards[value](self.game, value))

    def fill_and_shuffle_deck(self):
        [self.save_card(value) for value in self.cards]
        shuffle(self.deck)

    def get_and_pop_card(self):
        return self.deck.pop(0)


class Player:
    def __init__(self, start_card):
        self.card = start_card

    def move(self, dk):
        self.card = [self.card, dk.get_and_pop_card()]  # player take one more card
        self.choice_of_card()

    def card_selection(self):
        """return selected card"""
        return int(input(f'0({self.card[0].value}) или 1({self.card[1].value})'))

    def choice_of_card(self):
        choice = self.card_selection()
        if (self.card[0].value in [5, 6] or self.card[1].value in [5, 6]) and\
                (self.card[0].value == 7 or self.card[1].value == 7):
            while choice != 7:
                print("You can't discard this card")
                choice = self.card_selection()
        self.card[choice].move()  # discard one card
        self.card = self.card[(choice + 1) % 2]  # save other card


game = Game()
game.game_cycle()
