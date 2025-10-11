// LRU Cache in cpp

/*
The LRU Cache in cpp is implemented using an unordered_map and a doubly linked list.
We have the order with the list, and the map privides O(1) access.
The std::list also provides an iterator to the node.

Methods:
cache.find(key) -> returns an iterator to the key, or cache.end() if not found in O(1).
cache.erase(key) -> removes the key from the map in O(1).
cache.size() -> returns the number of elements in the map in O(1).

dll.push_front({key, value}) -> adds a new node with {key, value} at the front of the list in O(1).
dll.pop_back() -> removes the last node from the list in O(1).
dll.erase(key) -> removes the node pointed by the iterator key in O(1).
dll.begin() -> returns an iterator to the first node in the list in O(1).
dll.back() -> returns the last node in the list in O(1).

*/

#include <unordered_map>
#include <list>
using namespace std;

class LRUCache {
private:
    int capacity;
    // liste contenant des paires {clé, valeur}
    list<pair<int, int>> dll;  
    // hash map : clé -> itérateur vers le nœud correspondant dans la liste
    unordered_map<int, list<pair<int, int>>::iterator> cache;

public:
    LRUCache(int capacity) : capacity(capacity) {}

    int get(int key) {
        // clé absente du cache
        if (cache.find(key) == cache.end()) return -1;

        // récupère le nœud et le remet en tête (MRU)
        auto it = cache[key];
        int value = it->second;

        dll.erase(it);
        dll.push_front({key, value});
        cache[key] = dll.begin();

        return value;
    }

    void put(int key, int value) {
        // si la clé existe déjà → on l’enlève
        if (cache.find(key) != cache.end()) {
            dll.erase(cache[key]);
        }
        // insère en tête (MRU)
        dll.push_front({key, value});
        cache[key] = dll.begin();

        // dépassement de capacité → supprimer LRU
        if (cache.size() > capacity) {
            auto lru = dll.back();
            int lru_key = lru.first;
            dll.pop_back();
            cache.erase(lru_key);
        }
    }
};
