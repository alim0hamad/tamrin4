# حل هزارتو با جستجوی عمق اول (DFS)

maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0]
]

# 0 = راه آزاد ، 1 = دیوار
# شروع از (0,0) و پایان در (5,5)

rows = len(maze)
cols = len(maze[0])
start = (0, 0)
end = (5, 5)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # بالا، پایین، چپ، راست


def is_valid(x, y, visited):
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0 and not visited[x][y]


def dfs(x, y, path, visited):
    if (x, y) == end:
        path.append((x, y))
        return True

    visited[x][y] = True
    path.append((x, y))

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, visited):
            if dfs(nx, ny, path, visited):
                return True

    path.pop()  # بازگشت (backtrack)
    return False


def solve_maze():
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    path = []

    if dfs(start[0], start[1], path, visited):
        return path
    return None


def print_maze_with_path(path):
    display = [row[:] for row in maze]

    if path:
        for x, y in path:
            display[x][y] = 2  # مسیر پیدا شده

    print("هزارتو (۰=راه، ۱=دیوار، ۲=مسیر):")
    print()
    for row in display:
        line = ""
        for cell in row:
            if cell == 0:
                line += "·  "
            elif cell == 1:
                line += "█  "
            else:
                line += "●  "
        print(line)
    print()


# اجرا
path = solve_maze()

if path:
    print("مسیر پیدا شد:")
    print(" -> ".join([f"({x},{y})" for x, y in path]))
    print()
    print_maze_with_path(path)
else:
    print("مسیری پیدا نشد.")
