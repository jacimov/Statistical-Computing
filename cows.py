import sys
import os
from crowded_cows import find_crowded
import time


def main():
    if len(sys.argv) != 3:
        print("Usage: python cows.py K input_file")
        sys.exit(1)

    try:
        k = int(sys.argv[1])
        input_file = sys.argv[2]

        # Use relative path from script location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(script_dir, 'cows-data', input_file)

        start = time.time()

        # Read and process cows
        with open(data_path, 'r') as f:
            cows = [int(line.strip()) for line in f]

        result = find_crowded(cows, k)
        elapsed = time.time() - start

        print(f"Result: {result}")
        print(f"Time taken: {elapsed:.4f} seconds")

    except ValueError:
        print("Error: K must be an integer")
    except FileNotFoundError:
        print(f"Error: Could not find file {input_file}")


if __name__ == "__main__":
    main()
