//
// Created by Angela Xie on 12/5/20.
//

#include "Game.h"


Game::Game(string _gameName, string _state, string _date, int _count) {
    gameName = _gameName;
    state = _state;
    date = _date;
    count = _count;
}

void Game::print() {
    cout << gameName << " ";
    cout << state << " ";
    cout << date << " ";
    cout << count << " ";
    cout << endl;
}
