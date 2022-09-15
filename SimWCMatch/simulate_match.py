'''TODO: Module Docstring'''

# Define match simulation function
def simulate_match(win_probs):
    ''' TODO Docstring
    Input: win_probs, a 2D array of win probabilities. The first
    '''
    num_games = len(win_probs)
    # Make sure that each game has probabilities for all 3 last_results
    assert len(win_probs[0]) == 3
    # For each game
    for game in win_probs:
        # Make sure that the sum of probabilities is equal to 1
        assert sum(game) - 1 < .0001
    # An array storing the score distribution so far, mutates during simulation
     # Length should always be equal to 1 + (2 * NUM_GAMES_PLAYED)
    last_results = [1]
    # For each game
    for game in range(num_games):
        # Initialize an array storing the distribution of scores after this game
        next_results = [0 for i in range(2 * game + 3)]
        # For each possible prior state
        for last_result in range(len(last_results)):
            # For each possible result of the current game
            for result in range(3):
                # Increment the probability of the next result by the product of
                # the last result and the current result
                # TODO: shorten line
                next_results[last_result + result] += last_results[last_result] * win_probs[game][result]
        # Store the results of simulating this game
        last_results = next_results
    # Return the results after all games
    return last_results

def main():
    random_odds = [[0.35, 0.35, 0.30] for i in range(12)]
    x = simulate_match(random_odds)
    print("Win", round(sum(x[0:11]), 4))
    print("Draw", round(x[12], 4))
    print("Loss", round(sum(x[12:24]), 4))
    print(sum(x))

if __name__ == '__main__':
    main()
