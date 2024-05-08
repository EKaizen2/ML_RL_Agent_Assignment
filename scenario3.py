import numpy as np
from FourRooms import FourRooms

def main():
    # Create FourRooms Object
    fourRoomsObj = FourRooms('rgb',stochastic=True)

    # Set Hyperparameters
    alpha = 0.1  # Learning rate
    gamma = 0.9  # Discount factor
    epsilon = 0.1  # Exploration rate
    num_epoch = 100

    # Initialize Q-table
    Q = np.zeros((13, 13, 4))  # Q-table: 11x11 grid, 4 actions

    print('Training in progress...')

    aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']

    for epoc in range(num_epoch):
        # Reset the environment for a new epoch
        fourRoomsObj.newEpoch()
        state = fourRoomsObj.getPosition()
        done = False
        packages_collected = []

        print(f"Epoch ============================================================== {epoc + 1}")
        while not done:
            # Epsilon-greedy action selection
            if np.random.rand() < epsilon:
                action = np.random.choice([0, 1, 2, 3])  # Random action
            else:
                action = np.argmax(Q[state[1], state[0]])  # Greedy action

            # Take the chosen action
            grid_cell, next_pos, packages_remaining, done = fourRoomsObj.takeAction(action)

            # Ensure the next position stays within the boundaries
            next_pos = (min(max(next_pos[0], 1), 11), min(max(next_pos[1], 1), 11))

            # Print information
            print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[action], next_pos, gTypes[grid_cell]))

            # Collect packages in the correct order
            if grid_cell == 1:  # Red package
                if 'R' in packages_collected or 'G' in packages_collected or 'B' in packages_collected:
                    done = True
                else:
                    packages_collected.append('R')
            elif grid_cell == 2:  # Green package
                if 'R' not in packages_collected or 'G' in packages_collected or 'B' in packages_collected:
                    done = True
                else:
                    packages_collected.append('G')
            elif grid_cell == 3:  # Blue package
                if 'R' not in packages_collected or 'G' not in packages_collected or 'B' in packages_collected:
                    done = True
                else:
                    packages_collected.append('B')

            # Update Q-value
            old_Q = Q[state[1], state[0], action]
            if not done:
                new_Q = old_Q + alpha * (grid_cell + gamma * np.max(Q[next_pos[1], next_pos[0]]) - old_Q)
            else:
                new_Q = old_Q + alpha * (grid_cell - old_Q)  # Terminal state

            Q[state[1], state[0], action] = new_Q

            state = next_pos

        #print('Packages collected: ', packages_collected)

        # Decay epsilon
        epsilon = max(epsilon * 0.99, 0.01)

    print('Training completed.')

    # Show the final Path
    fourRoomsObj.showPath(-1)
    # Save the final Path
    fourRoomsObj.showPath(-1, savefig="scenario3_path.png")


if __name__ == "__main__":
    main()
