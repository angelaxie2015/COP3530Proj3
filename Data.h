#include "Game.h"
#include <unordered_map>
#ifndef COP3530PROJ3_DATA_H
#define COP3530PROJ3_DATA_H


class Data {
    vector<Game> data;
    unordered_map<string, int> m; //string: state name, int: index in the array.

public:
    void insert(Game g);
    vector<Game> getstate(string stateName);
    vector<Game> getDate(string date);
    vector<pair<string, Game>> getDateCount(vector<Game>& games, string date);



};


#endif //COP3530PROJ3_DATA_H
