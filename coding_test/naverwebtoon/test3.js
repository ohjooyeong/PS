function solution(block, board) {
    let tet = [
        [
            [0, 0],
            [1, 0],
            [2, 0],
        ],
        [
            [0, 0],
            [0, 1],
            [0, 2],
        ],
        [
            [0, 0],
            [1, 0],
            [1, 1],
        ],
        [
            [0, 0],
            [1, 0],
            [-1, -1],
        ],
        [
            [0, 0],
            [0, 1],
            [1, 1],
        ],
        [
            [0, 0],
            [0, 1],
            [1, 0],
        ],
    ];
    var answer = 0;
    let sero = board.length;
    let garo = board[0].length;
    for (let i = 0; i < sero; i++) {
        for (let j = 0; j < garo; j++) {
            for (let t in tet[block]) {
                let x = i + t[0];
                let y = j + t[1];
                if (0 <= x && x < sero && 0 <= y && y < garo) {
                }
            }
        }
    }
    return answer;
}
