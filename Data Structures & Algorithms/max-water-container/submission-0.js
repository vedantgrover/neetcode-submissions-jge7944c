class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let maxHeight = 0;

        for (let i = 0; i < heights.length - 1; i++) {
            for (let j = i + 1; j < heights.length; j++) {
                let area = (j - i) * Math.min(heights[i], heights[j]);
                console.log("Area", area);

                if (area > maxHeight) {
                    maxHeight = area;
                } 
            }
        }

        return maxHeight;
    }
}
