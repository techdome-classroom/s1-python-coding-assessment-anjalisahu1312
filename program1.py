class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here

    def num_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    # Function to perform DFS and mark connected land as water
    def dfs(row, col):
        # Check boundaries and ensure the current cell is land
        if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 'W':
            return

        # Mark the current cell as water to avoid revisiting
        grid[row][col] = 'W'

        # Explore all four directions (up, down, left, right)
        dfs(row + 1, col)  # down
        dfs(row - 1, col)  # up
        dfs(row, col + 1)  # right
        dfs(row, col - 1)  # left

    # Traverse the entire grid
    for row in range(rows):
        for col in range(cols):
            # If we encounter land, start a new DFS to mark the entire island
            if grid[row][col] == 'L':
                island_count += 1
                dfs(row, col)

    return island_count

# Test Cases
map1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]

map2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"],
]

print(num_islands(map1))  # Output: 1
print(num_islands(map2))  # Output: 3
                    
    
