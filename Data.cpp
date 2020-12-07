#include "Data.h"

void Data::insert(Game g) {
    data.push_back(g);
}

vector<Game> Data::getstate(string stateName) {
    vector<Game> ans;
    for(Game& temp: data){
        if(temp.state == stateName){
            ans.push_back(temp);
        }
    }
    return ans;
}

vector<Game> Data::getDate(string date) {
    vector<Game> ans;
    for(Game& temp: data){
        if(temp.date == date){
            ans.push_back(temp);
        }
    }
    return ans;
}

vector<Game> Data::getDateCount(string date) {
    vector<Game> list = getDate(date);
    vector<Game> ans;
    unordered_map<string, int> m; //string: game name, int: total count associated with the game

    for(Game& game: list){
        m[game.gameName] += game.count;
    }

    for(auto& iter: m){
        Game temp(iter.first, "TEMP", date, iter.second);
        ans.push_back(temp);
    }

    return ans;
}

vector<Game> Data::getStateDateCount(string state, string date) {
    vector<Game> ans;

    for(Game& game: data){
        if(game.state == state && game.date == date)
            ans.push_back(game);
    }

    return ans;
}
