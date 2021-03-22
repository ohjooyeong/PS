# 크레인 인형뽑기 게임


def pick(board, move):
    res = 0
    for i in range(len(board)):
        if board[i][move - 1] > 0:
            res = board[i][move - 1]
            board[i][move - 1] = 0
            return res
    return res


def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        res = pick(board, move)
        if res > 0:
            if len(basket) > 0 and basket[-1] == res:
                answer += 2
                basket.pop()
            else:
                basket.append(res)
    return answer


# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# moves = [1,5,3,5,1,2,1,4]
# print(solution(board, moves))
