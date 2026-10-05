class TimeMap {
public:
    TimeMap() {
         
    }
    
    void set(string key, string value, int timestamp) {
        hashmap[key].push_back(std::make_pair(timestamp, value));
    }
    
    string get(string key, int timestamp) {
        if (hashmap.count(key) == 0) return "";
        int l = 0, r = hashmap[key].size()-1;
        while (l <= r) {
            int mid = l + (r-l) / 2;
            if (timestamp == hashmap[key][mid].first) {
                return hashmap[key][mid].second;
            }
            else if (timestamp > hashmap[key][mid].first) {
                l = mid + 1;
            }
            else {
                r = mid - 1;
            }
        }
        return (r < 0) ? "" : hashmap[key][r].second;
        
    }
    private:
    std::unordered_map<string, std::vector<std::pair<int,string>>> hashmap;
};
