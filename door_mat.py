def door_mat(rows, cols):

    for i in range(1, rows, 2):
        pattern = ".|." * i
        print(pattern.center(cols, "-"))

    print("WELCOME".center(cols, "-"))

    for i in range(rows - 2, 0, -2):
        pattern = ".|." * i
        print(pattern.center(cols, "-"))

if __name__ == "__main__":
    N, M = map(int, input().split())
    door_mat(N, M)