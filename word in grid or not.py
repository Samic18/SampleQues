'''
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i,j, count):
            if count == len(word): return True
            if 0<=i<len(board) and 0<=j<len(board[0]) and board[i][j] == word[count]:
                
                tmp = board[i][j]
                board[i][j] = "#"
                moves = [(1,0),(-1,0),(0,1),(0,-1)]

                for dx, dy in moves:
                    if dfs(i+dx, j+dy, count+1):
                        return True
                board[i][j] = tmp            
                return False
            
            
            
            
            '''The complexity will be O(m∗n∗4s) where m is the no. of rows and n is the no. of columns in the 2D matrix and s is the length of the input string.

When we start searching from a character we have 4 choices of neighbors for the first character and subsequent characters have only 3 or less than 3 choices but we can take it as 4 (permissible slopiness in upper bound). This slopiness would be fine in large matrices. So for each character we have 4 choices. Total no. of characters are s where s is the length of the input string. So one invocation of search function of your implementation would take O(4s) time.

Also in worst case the search is invoked for m∗n times. So an upper bound would be O(m∗n∗4s).'''
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]== word[0] and dfs(i,j,0) :
                    return True
        return False
