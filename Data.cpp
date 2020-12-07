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
    vector<Game> list = getDate(data);
    vector<Game> ans;
    unordered_map<string, int> m;

    for(Game& game: list){
        m[game.gameName] += game.count;
    }

    for(auto& iter: map){
        Game temp(iter.first, "TEMP", date, iter.second);
        ans.push_back(temp);
    }

    return ans;
}