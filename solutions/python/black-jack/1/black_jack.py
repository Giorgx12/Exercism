"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""



def value_of_card(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1  # L'asso vale 1 per ora
    else:
        return int(card)


def value_of_card(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1  # For now, ace is 1
    else:
        return int(card)

def higher_card(card_one, card_two):
    value1 = value_of_card(card_one)
    value2 = value_of_card(card_two)

    if value1 > value2:
        return card_one
    elif value2 > value1:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    
    # Se uno dei due è già un asso, il nuovo asso deve valere 1
    if card_one == 'A' or card_two == 'A':
        return 1
    
    # Se 11 può essere aggiunto senza superare 21, usalo, altrimenti usa 1
    if total + 11 <= 21:
        return 11
    else:
        return 1



def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if card_one in ['J', 'Q', 'K']:
        num1 = 10
    elif card_one == 'A':
        num1 = 11  # For now, ace is 1
    else:
        num1 = int(card_one)
    if card_two in ['J', 'Q', 'K']:
        num2 = 10
    elif card_two == 'A':
        num2 = 11  # For now, ace is 1
    else:
        num2 = int(card_two)
    if num1 + num2 == 21:
        return True
    if num1 + num2 != 21:
        return False



def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    if card_one in ['J', 'Q', 'K']:
        num1 = 10
    elif card_one == 'A':
        num1 = 11  # For now, ace is 1
    else:
        num1 = int(card_one)
    if card_two in ['J', 'Q', 'K']:
        num2 = 10
    elif card_two == 'A':
        num2 = 11  # For now, ace is 1
    else:
        num2 = int(card_two)
    if num1 == num2:
        return True
    else:
        return False
    


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    if card_one in ['J', 'Q', 'K']:
        num1 = 10
    elif card_one == 'A':
        num1 = 1  # For now, ace is 1
    else:
        num1 = int(card_one)
    if card_two in ['J', 'Q', 'K']:
        num2 = 10
    elif card_two == 'A':
        num2 = 1  # For now, ace is 1
    else:
        num2 = int(card_two)
    if num1 + num2 == 9 or num1 + num2 == 10 or num1 + num2 == 11:
        return True
    else:
        return False
