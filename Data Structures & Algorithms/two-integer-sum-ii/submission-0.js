class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let maxIndex = numbers.length;

        for (let i = 0; i < numbers.length; i++) {
            const currentSum = numbers[i];
            for (let j = i+1; j < maxIndex; j++) {
                const sum = currentSum + numbers[j];

                if (sum > target) {
                    maxIndex = j
                }

                if (sum === target) {
                    return [i + 1, j + 1];
                }
            }
        }
    }
}
