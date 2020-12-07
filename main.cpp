#include <iostream>
#include <SFML/Graphics.hpp>
#include "Data.h"
#include <string>
#include <fstream>
using namespace std;



void loadFile(const string fileName, Data& d){ //reading the file and inserting it into Data
    ifstream file;
    file.open(fileName);
    string fileInput;
    vector<string> dates;

    //1. storing the dates in a date vector
    getline(file, fileInput);
    int index= fileInput.find_first_of(',');
    fileInput = fileInput.substr(index+1);
    index = fileInput.find_first_of(',');
    fileInput = fileInput.substr(index+1);

    while(fileInput.find_first_of(',') != -1){ //storing all the dates
        index = fileInput.find_first_of(',');
        dates.push_back(fileInput.substr(0, index));
        fileInput = fileInput.substr(index+1);
    }

    //2. reading the rest of the data and push to games to use
    while(!file.eof()){
        getline(file, fileInput);

        //i. storing state
        index = fileInput.find_first_of(',');
        string state = fileInput.substr(0, index);
        fileInput = fileInput.substr(index+1);

        //ii. storing game name
        index = fileInput.find_first_of(',');
        string gameName = fileInput.substr(0, index);
        fileInput = fileInput.substr(index+1);

        //iii. loop through rest of the line storing date & storing counts
        int i = 0; //index to loop through the dates vector to assign values
        while(fileInput.find_first_of(',') != -1){ //storing all the dates
            index = fileInput.find_first_of(',');
            string date = dates[i++];

            int count = stoi(fileInput.substr(0, index));
            fileInput = fileInput.substr(index+1);

            //iv. create a game class and store in data
            Game g(gameName, state, date, count);
            d.insert(g);

            i = (i == dates.size()) ? 0 : i; //checking index to match the dates
        }
    }
}


int main() {
    std::cout << "Hello, World!" << std::endl;
    string loc = "../project3/search_trends7.csv";
    Data data;

    //1. read file and store in an array of games
    loadFile(loc, data);

    vector<Game> temp = data.getDate("6/1/19");
    for(Game& g: temp)
        g.print();

    //2. use a map to match index with game name & have a vector of counts

    //3. sort

    //4. display
    sf::RenderWindow window(sf::VideoMode(800, 600), "GoogleTrends");






    return 0;
}
