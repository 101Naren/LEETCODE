class Solution {
public:
    vector<vector<int>> ans;

    void backtrack(vector<int>& candidates,
                   int target,
                   int start,
                   vector<int>& current) {

        if (target == 0) {
            ans.push_back(current);
            return;
        }

        if (target < 0) {
            return;
        }

        for (int i = start; i < candidates.size(); i++) {

            // Skip duplicate values at the same level
            if (i > start && candidates[i] == candidates[i - 1])
                continue;

            current.push_back(candidates[i]);

            // i + 1 because each element can be used only once
            backtrack(candidates,
                      target - candidates[i],
                      i + 1,
                      current);

            current.pop_back(); // backtrack
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {

        sort(candidates.begin(), candidates.end());

        vector<int> current;

        backtrack(candidates, target, 0, current);

        return ans;
    }
};