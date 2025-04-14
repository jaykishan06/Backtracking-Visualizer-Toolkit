def n_queens(n):
    board = [-1] * n

    def is_safe(row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(row):
        if row == n:
            print("Solution:", board)
            return True
        for col in range(n):
            print(f"Trying Queen at row {row}, col {col}")
            if is_safe(row, col):
                board[row] = col
                print(f"Placed Queen at ({row}, {col})")
                if solve(row + 1):
                    return True
                print(f"Backtracking from ({row}, {col})")
                board[row] = -1
        return False

    solve(0)

def subset_sum(arr, target):
    result = []

    def backtrack(i, current, total):
        print(f"Index: {i}, Current Set: {current}, Total: {total}")
        if total == target:
            print("Found Subset:", current)
            result.append(current[:])
            return
        if i >= len(arr) or total > target:
            return
        current.append(arr[i])
        backtrack(i + 1, current, total + arr[i])
        current.pop()
        backtrack(i + 1, current, total)

    backtrack(0, [], 0)

def main():
    print("Backtracking Visualizer Toolkit")
    print("1. N-Queens")
    print("2. Subset Sum")

    choice = input("Choose a problem (1-2): ")

    if choice == '1':
        n = int(input("Enter number of queens (n): "))
        n_queens(n)
    elif choice == '2':
        arr = list(map(int, input("Enter the set (space-separated): ").split()))
        target = int(input("Enter the target sum: "))
        subset_sum(arr, target)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
