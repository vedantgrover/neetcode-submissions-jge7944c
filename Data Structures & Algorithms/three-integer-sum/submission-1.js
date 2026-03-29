class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        let result = [];
        const target = 0;
        nums.sort((a, b) => a - b);
        console.log("Nums", nums);

        for (let i = 0; i < nums.length; i++) {
            if (i > 0) {
                if (nums[i] === nums[i - 1]) {
                    continue;
                }
            }

            let l = i + 1;
            let r = nums.length - 1;

            while (l < r) {
                let sum = nums[i] + nums[l] + nums[r];

                if (sum == target) {
                    result.push([nums[i], nums[l], nums[r]]);
                    l++;
                    while (nums[l] == nums[l - 1]) {
                        l++;
                    }
                } else if (sum < target) {
                    l++;
                } else {
                    r--;
                }
            }
        }

        return result;
    }
}
