class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let maxArea = 0;

        let l = 0;
        let r = heights.length - 1;

        while (l < r) {
            let area = (r - l) * Math.min(heights[l], heights[r]);

            maxArea = Math.max(maxArea, area);

            if (Math.min(heights[l], heights[r]) == heights[l]) {
                l++;
            } else {
                r--;
            }
        }

        // for (let i = 0; i < heights.length - 1; i++) {
        //     for (let j = i + 1; j < heights.length; j++) {
        //         let area = (j - i) * Math.min(heights[i], heights[j]);
        //         console.log("Area", area);

        //         if (area > maxHeight) {
        //             maxHeight = area;
        //         } 
        //     }
        // }

        return maxArea;
    }
}
