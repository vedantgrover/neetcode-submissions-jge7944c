class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let maxProfit = 0;

        let l = 0;
        let r = 1;

        while (r < prices.length) {
            let difference = prices[r] - prices[l];
            if (difference <= 0) {
                l = r;
            } else {
                maxProfit = Math.max(maxProfit, difference);
            }
            r++;
        }
        // for (let i = 0; i < prices.length - 1; i++) {
        //     for (let j = i + 1; j < prices.length; j++) {
        //         maxProfit = Math.max(maxProfit, prices[j] - prices[i])
        //     }
        // }

        return maxProfit;
    }
}
