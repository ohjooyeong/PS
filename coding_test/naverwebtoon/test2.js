function solution(money, cost) {
    var answer = 0;
    let totcost = [];
    cost.reduce(function (a, b, i) {
        return (totcost[i] = a + b);
    }, 0);
    let start = 0;
    let end = 0;
    while (true) {
        if (totcost[end] - totcost[start] >= money) {
            start++;
        } else if (end == cost.length || start === cost.length) {
            break;
        } else if (cost[start] > money) {
            start++;
        } else {
            answer = Math.max(answer, end - start + 1);
            end++;
        }
    }
    return answer;
}
money = 420;
cost = [0, 900, 0, 200, 150, 0, 30, 50];
console.log(solution(money, cost));
