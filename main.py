# Import files and methods for main function

import argparse
from FourRooms import FourRooms
import scenario1
import scenario2
import scenario3



def main():
    parser = argparse.ArgumentParser(description='RL Algorithm for Four Rooms Environment')
    parser.add_argument('-scenario', type=str, choices=['simple', 'multi', 'rgb'], default='simple',
                        help='Specifies the scenario: simple, multi, or rgb')
    parser.add_argument('-stochastic', action='store_true', help='Enables stochastic action space')

    args = parser.parse_args()

    # Create FourRooms Object with specified scenario and stochasticity
    fourRoomsObj = FourRooms(args.scenario, stochastic=args.stochastic)

    # Calling the appropriate scenario function based on the specified scenario
    if args.scenario == 'simple':
        scenario1.main()
    elif args.scenario == 'multi':
        scenario2.main()
    elif args.scenario == 'rgb':
        scenario3.main()

if __name__ == "__main__":
    main()
