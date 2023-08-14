/*
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
*/

class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int target = int(graph.size()) - 1;
        vector<int> path{0};
        vector<vector<int>> results;

        function<void(int, vector<int>&)> backtrack = [&](int currNode, vector<int>& path) {
            if (currNode == target) {
                results.push_back(vector(path));
                return;
            }
            for (int nextNode : graph[currNode]) {
                path.push_back(nextNode);
                backtrack(nextNode, path);
                path.pop_back();
            }
        };

        backtrack(0, path);
        return results;
    }
};