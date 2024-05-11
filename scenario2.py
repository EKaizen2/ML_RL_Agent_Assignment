from FourRooms import FourRooms
import numpy as np

def main():
    # Create FourRooms Object
    fourRoomsObj = FourRooms('multi',stochastic=True)

    # Set Hyperparameters
    alpha = 0.1  # Learning rate
    gamma = 0.9  # Discount factor
    epsilon = 0.1  # Exploration rate
    num_epoch = 100

    # Initialize Q-table
    Q = np.zeros((13, 13, 4))  # Q-table: 11x11 grid, 4 actions

    aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']

    print('Training in progress...')

    for episode in range(num_epoch):
        # Reset the environment for a new epoch
        fourRoomsObj.newEpoch()
        state = fourRoomsObj.getPosition()
        done = False
        
        print(f"Epoch ============================================ {episode + 1}/{num_epoch}")
        while not done:
            # Epsilon-greedy action selection
            if np.random.rand() < epsilon:
                action = np.random.choice([0, 1, 2, 3])  # Random action
            else:
                action = np.argmax(Q[state[1], state[0]])  # Greedy action
            
            # Take the chosen action
            if not done:  # Ensure not in terminal state before taking action
                grid_cell, next_pos, _, done = fourRoomsObj.takeAction(action)
                next_pos = (min(max(next_pos[0], 1), 11), min(max(next_pos[1], 1), 11))  # Ensure position is within boundaries

                print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[action], next_pos, gTypes[grid_cell]))

                # Update Q-value
                old_Q = Q[state[1], state[0], action]
                if not done:
                    new_Q = old_Q + alpha * (grid_cell + gamma * np.max(Q[next_pos[1], next_pos[0]]) - old_Q)
                else:
                    new_Q = old_Q + alpha * (grid_cell - old_Q)  # Terminal state
                
                Q[state[1], state[0], action] = new_Q
                
                state = next_pos
        
        # Decay epsilon
        epsilon = max(epsilon * 0.99, 0.01)

    print('Training completed.')

    # Run the learned policy
    # print('Running learned policy...')
    # state = fourRoomsObj.getPosition()
    # done = False
    # while not done:
    #     action = np.argmax(Q[state[1], state[0]])  # Greedy action
    #     if not done:  # Ensure not in terminal state before taking action
    #         grid_cell, next_pos, _, done = fourRoomsObj.takeAction(action)
    #         print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[action], next_pos, gTypes[grid_cell]))
    #         state = next_pos

    # Show the final Path
    fourRoomsObj.showPath(-1)

    # Save the final Path Image
    fourRoomsObj.showPath(-1, savefig="scenario2_path.png")

if __name__ == "__main__":
    main()
