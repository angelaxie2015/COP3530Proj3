#include "iostream"
#include "string"
#include "unordered_map"
#include "vector"
using namespace std;

#ifndef COP3530PROJ3_GAME_H
#define COP3530PROJ3_GAME_H


class Game {


public:
    string gameName;
    string state;
    string date;
    int count;
    Game(string _gameName, string _state, string _date, int _count);
    void print();

};


#endif //COP3530PROJ3_GAME_H
