import argparse, importlib

def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2024 Solver")
    parser.add_argument("-d", "--day", type=int, required=True, help="Day of the challenge")
    parser.add_argument("-p", "--part", type=int, choices=[1, 2], help="Part of the challenge (1 or 2)")

    args = parser.parse_args()

    solution = importlib.import_module(f"day{args.day}.main").solution(args.day, args.part)
    solution.solve()
    
if __name__ == "__main__":
    main()