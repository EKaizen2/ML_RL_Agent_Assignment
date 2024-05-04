import numpy as np
from FourRooms import FourRooms

def main():
    # Create FourRooms Object
    fourRoomsObj = FourRooms('simple')

    # Hyperparameters
    alpha = 0.1  # Learning rate
    gamma = 0.9  # Discount factor
    epsilon = 0.1  # Exploration rate
    num_epoch = 100

    # Initialize Q-table
    num_actions = 4  # Number of actions (UP, DOWN, LEFT, RIGHT)
    Q = np.zeros((11, 11, num_actions))  # Q-table: 11x11 grid, 4 actions

    print('Training in progress...')
    for epoc in range(num_epoch):
        # Reset the environment for a new epoch
        fourRoomsObj.newEpoch()
        state = fourRoomsObj.getPosition()
        done = False
        
        print(f"Epoch ============================================================== {epoc+1}")
        while not done:
            # Epsilon-greedy action selection
            if np.random.rand() < epsilon:
                action = np.random.randint(num_actions)  # Random action
            else:
                action = np.argmax(Q[state[1], state[0]])  # Greedy action
            
            # Take the chosen action
            grid_cell, next_pos, _, done = fourRoomsObj.takeAction(action)
            
            # Ensure the next position stays within the boundaries
            next_pos = (min(max(next_pos[0], 1), 10), min(max(next_pos[1], 1), 10))

            # Print information
            # print(f"Action: {action}, Next position: {next_pos}, Done: {done}")

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

    # Evaluation
    print('Evaluating the learned policy...')
    success_count = 0
    total_epoch = 100

    for _ in range(total_epoch):
        fourRoomsObj.newEpoch()
        state = fourRoomsObj.getPosition()
        done = False

        while not done:
            action = np.argmax(Q[state[1], state[0]])  # Greedy action
            _, next_pos, _, done = fourRoomsObj.takeAction(action)
            state = next_pos

        if done:
            success_count += 1

    success_rate = success_count / total_epoch
    print(f'Success rate of Learned Policy: {success_rate:.2%}')

    # Show the final Path
    fourRoomsObj.showPath(-1)
    # Save the final Path
    fourRoomsObj.showPath(-1, savefig="scenario1_path.png")


if __name__ == "__main__":
    main()
