#include <iostream>
#include <vector>
#include <utility>
#include <fstream>
#include <tuple>
#include <map>
#include <queue>
#include <set>
#include <limits>

using namespace std;

class Solution
{
private:
    vector<string> grid;
    vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    pair<int, int> start = {-1, -1};
    pair<int, int> end = {-1, -1};
    map<tuple<int, int, int>, int> dist;
    map<tuple<int, int, int>, vector<tuple<int, int, int>>> predecessors;

    void parse(const string &fileName)
    {
        ifstream fin(fileName);
        string line;
        int r = 0;

        while (getline(fin, line))
        {
            grid.push_back(line);
            for (int c = 0; c < static_cast<int>(line.size()); c++)
            {
                if (line[c] == 'S')
                    start = {r, c};
                if (line[c] == 'E')
                    end = {r, c};
            }
            r++;
        }

        if (start == make_pair(-1, -1) || end == make_pair(-1, -1))
        {
            cerr << "Error: Start (S) or End (E) point not found in the grid." << endl;
            exit(1);
        }
    }

    uint64_t dijkstra()
    {
        priority_queue<tuple<int, int, int, int>, vector<tuple<int, int, int, int>>, greater<tuple<int, int, int, int>>> pq;
        pq.push({0, start.first, start.second, -1}); // distance, row, col, direction
        dist[{start.first, start.second, -1}] = 0;

        while (!pq.empty())
        {
            auto [d, r, c, dir] = pq.top();
            pq.pop();

            if (grid[r][c] == 'E')
                return d;

            for (int i = 0; i < 4; i++)
            {
                int nr = r + directions[i].first;
                int nc = c + directions[i].second;
                int nd = d + 1;

                if (i != dir && dir != -1)
                    nd += 1000;

                if (nr < 0 || nc < 0 || nr >= static_cast<int>(grid.size()) || nc >= static_cast<int>(grid[0].size()) || grid[nr][nc] == '#')
                    continue;

                auto current = make_tuple(nr, nc, i);
                if (dist.find(current) == dist.end() || nd < dist[current])
                {
                    dist[current] = nd;
                    pq.push({nd, nr, nc, i});
                    predecessors[current].clear();
                    predecessors[current].push_back({r, c, dir});
                }
                else if (nd == dist[current])
                {
                    predecessors[current].push_back({r, c, dir});
                }
            }
        }

        return numeric_limits<uint64_t>::max();
    }

    uint64_t backtrack()
    {
        set<pair<int, int>> unique_tiles;
        queue<tuple<int, int, int>> q;

        for (int i = 0; i < 4; i++)
            q.push({end.first, end.second, i});

        while (!q.empty())
        {
            auto [r, c, dir] = q.front();
            q.pop();

            unique_tiles.insert({r, c});

            for (const auto &pred : predecessors[{r, c, dir}])
            {
                q.push(pred);
            }
        }

        return unique_tiles.size();
    }

public:
    Solution(const string &fileName)
    {
        parse(fileName);
    }

    uint64_t part1()
    {
        return dijkstra();
    }

    uint64_t part2()
    {
        dijkstra();
        return backtrack();
    }
};

int main()
{
    Solution solution("day16.txt");

    cout << "Part 1: " << solution.part1() << endl;
    cout << "Part 2: " << solution.part2() << endl;

    return 0;
}
