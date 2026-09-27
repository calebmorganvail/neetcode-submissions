impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n: usize = nums.len();
        let mut r: Vec<i32> = vec![1; n];

        let mut prefix: i32 = 1;
        for i in 0..n {
            r[i] = prefix;
            prefix *= nums[i];
        }

        let mut postfix: i32 = 1;
        for i in (0..n).rev() {
            r[i] *= postfix;
            postfix *= nums[i];
        }

        r
    }
}
