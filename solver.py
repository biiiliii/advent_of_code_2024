import argparse, importlib
import time

def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2024 Solver")
    parser.add_argument("-d", "--day", type=int, required=True, help="Day of the challenge")
    parser.add_argument("-p", "--part", type=int, choices=[1, 2], help="Part of the challenge (1 or 2)")
    parser.add_argument("-t", "--time", action="store_true", help="Measure execution time")

    args = parser.parse_args()

    solution = importlib.import_module(f"day{args.day}.main").solution(args.day, args.part)
    
    if args.time:
        start_time = time.time()
        solution.solve()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
    else:
        solution.solve()
    
if __name__ == "__main__":
    main()