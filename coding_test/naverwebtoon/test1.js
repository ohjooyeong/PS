function solution(k, rates) {
    let answer = 0;
    let dollar = 0;
    function invest(L, cnt, won, dollar) {
        if (L == cnt) {
            answer = Math.max(answer, won);
            return;
        } else {
            if (dollar == 0) {
                if (won >= rates[cnt]) {
                    invest(L, cnt + 1, won - rates[cnt], 1);
                    invest(L, cnt + 1, won, 0);
                } else {
                    invest(L, cnt + 1, won, 0);
                }
            } else {
                invest(L, cnt + 1, won + rates[cnt], 0);
                invest(L, cnt + 1, won, 1);
            }
        }
    }
    invest(rates.length, 0, k, dollar);

    return answer;
}
k = 1500;
rates = [1500, 1400, 1300, 1200];

console.log(solution(k, rates));
