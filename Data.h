#include "Game.h"
#ifndef COP3530PROJ3_DATA_H
#define COP3530PROJ3_DATA_H


class Data {
    vector<Game> data;

public:
    void insert(Game g);
    vector<Game> getstate(string stateName);



};


#endif //COP3530PROJ3_DATA_H
