import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(cards):
    """Returns the current score. Adjusts for Aces."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player, dealer):
    if player == dealer:
        return "Draw "
    elif dealer == 0:
        return "Lose, dealer has Blackjack "
    elif player == 0:
        return "Win with a Blackjack "
    elif player > 21:
        return "You went over. You lose "
    elif dealer > 21:
        return "Dealer went over. You win "
    elif player > dealer:
        return "You win "
    else:
        return "You lose "

def play_game():
    print("Welcome to Blackjack!")
    
    player_cards = []
    dealer_cards = []

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            draw = input("Type 'y' to get another card, 'n' to pass: ")
            if draw == 'y':
                player_cards.append(deal_card())
            else:
                game_over = True

    while calculate_score(dealer_cards) < 17 and calculate_score(dealer_cards) != 0:
        dealer_cards.append(deal_card())

    print(f"Your final hand: {player_cards}, final score: {calculate_score(player_cards)}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")
    print(compare(calculate_score(player_cards), calculate_score(dealer_cards)))

if __name__ == "__main__":
    play_game()
