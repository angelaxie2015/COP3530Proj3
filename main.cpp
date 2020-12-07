#include <iostream>
#include <SFML/Graphics.hpp>
#include "Data.h"
#include <string>
#include <fstream>
#include <vector>
using namespace std;

vector<Game> bubbleSort(vector<Game> targetVec) {
    vector<Game> res = targetVec;

    for (int i = 0; i < res.size() - 1; i++) {
        int swapped = 0;

        for (int j = 0; j < res.size() - i - 1; ++j) {
            if (res[j].count > res[j + 1].count) {
                swap(res[j], res[j + 1]);
                swapped = 1;
            }
        }
        if (swapped == 0)
            break;
    }
    return res;
}

vector<Game> insertionSort(vector<Game> targetVec) {
    vector<Game> res = targetVec;

    for (int i = 1; i < res.size(); i++) {
        Game key = res[i];
        int keyCount = key.count;

        int j = i - 1;

        while (keyCount < res[j].count && j >= 0) {
            res[j + 1] = res[j];
            j--;
        }
        res[j + 1] = key;
    }
    return res;
}

vector<Game> selectionSort(vector<Game> targetVec) {
    vector<Game> res = targetVec;

    for (int i = 0; i < res.size() - 1; i++) {
        int min_index = i;

        for (int j = i + 1; j < res.size(); j++) {
            if (res[j].count < res[min_index].count)
                min_index = j;
        }
        swap(res[min_index], res[i]);
    }
    return res;
}

int partition (vector<Game>& data, int low, int high)
{
    int pivot = data[high].count;
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++){
        if (data[j].count < pivot){
            i++;
            swap(data[i], data[j]);
        }
    }

    swap(data[i + 1], data[high]);
    return (i + 1);
}

vector<Game> quickSort(vector<Game>& data, int low, int high)
{
    //low = 0, high = size()-1
    if (low < high){
        int pivot = partition(data, low, high);
        quickSort(data, low, pivot - 1);
        quickSort(data, pivot + 1, high);
    }
    return data;
}

void heapify (vector<Game>& data, int i, int len) {
    int max = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < len && data[left].count > data[max].count)
        max = left;

    if (right < len && data[right].count > data[max].count)
        max = right;

    if (max != i){
        swap(data[i], data[max]);
        heapify(data, max, len);
    }
}

vector<Game> heapSort (vector<Game>& data) {
    int len = data.size();

    for(int i = (data.size() - 1) / 2; i >= 0; i--)
        heapify(data, i, data.size());

    for(int i = data.size() - 1; i >= 1; i--) {
        swap(data[0],data[i]);
        len--;
        heapify(data, 0, len);
    }
    return data;
}

void loadFile(const string fileName, Data& d, vector<string>& dates){ //reading the file and inserting it into Data
    ifstream file;
    file.open(fileName);
    string fileInput;

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

void printText(sf::RenderWindow& window, float y, string str){ //printing the name of the ranking games
    sf::Text text;
    sf::Font font;

    if (!font.loadFromFile("Aaweiweidianzhenti.ttf")) //checking whether font is correctly loaded.
    {
        cout << "Error" << endl;
    }

    text.setString(str);
    text.setCharacterSize(40);
    text.setFont(font);
    text.setColor(sf::Color::White);
    text.setPosition(50,y);

    window.draw(text);
}

void printBar(sf::RenderWindow& window, float yPos, float width){
    sf::RectangleShape rectangle(sf::Vector2f(width, 70));
    rectangle.setPosition(500, yPos);
    sf::RectangleShape rectBack(sf::Vector2f(1000,20));
    rectBack.setPosition(500, yPos+20);
    window.draw(rectangle);
}

int main() {
    //std::cout << "Hello, World!" << std::endl;
    string loc = "../project3/search_trends7.csv";
    Data data;

    //1. read file and store in an array of games
    vector<string> dates;
    loadFile(loc, data, dates);



    //2. sort
    cout << "Which state do you want to take a look at?" << endl;
    string state;
    cin >> state;
/*
    vector<Game> givenState = data.getstate(state);

    clock_t t;
    t = clock();
    printf ("Calculating...\n");
    vector<Game> heapsortList = heapSort(givenState); //sorting using heapsort
    t = clock() - t;
    cout << "It took " << ((float)t)/CLOCKS_PER_SEC << " to do heap sort." << endl;

    vector<Game> bubblesortList = bubbleSort(givenState); //sorting using bubble sort
    t = clock() - t;
    cout << "It took " << ((float)t)/CLOCKS_PER_SEC << " to do bubble sort." << endl;

    vector<Game> insertionList = insertionSort(givenState);
    t = clock() - t;
    cout << "It took " << ((float)t)/CLOCKS_PER_SEC << " to do insertion sort." << endl;

    vector<Game> selectionList = selectionSort(givenState);
    t = clock() - t;
    cout << "It took " << ((float)t)/CLOCKS_PER_SEC << " to do selection sort." << endl;

    vector<Game> quicklist = quickSort(givenState, 0 , givenState.size() - 1);
    t = clock() - t;
    cout << "It took " << ((float)t)/CLOCKS_PER_SEC << " to do quick sort." << endl;

    cout << "Highes search is " << quicklist[quicklist.size() - 1].gameName << " on " << quicklist[quicklist.size() - 1].date << " with " << quicklist[quicklist.size() - 1].count << " searches." << endl;

  */

    //3. display
    int width = 2000;
    int height = 1650;
    sf::RenderWindow window(sf::VideoMode(width, height), "GoogleTrends");

    window.setFramerateLimit(3); //setting framerate to be slower.

    while (window.isOpen())
    {
        // check all the window's events that were triggered since the last iteration of the loop
        sf::Event event;
        while (window.pollEvent(event))
        {
            // "close requested" event: we close the window
            if (event.type == sf::Event::Closed)
                window.close();
        }

        sf::Text text;
        sf::Font font1;
        if (!font1.loadFromFile("1574926762.ttf"))
        {
            cout << "Error" << endl;
        }

        //1. iterate through the dates and draw a different thing for each date:
        // draw everything here...
        for(string& date: dates) {
            window.clear(sf::Color::Black);
            text.setString(date);
            text.setCharacterSize(100);
            text.setFont(font1);
            text.setStyle(sf::Text::Bold);
            window.draw(text);

            vector<Game> list = data.getStateDateCount(state, date);
            vector<Game> sorted = heapSort(list); //sorting list based on the given state

            int yLoc = 130;
            for(int i = sorted.size() - 1; i >= 6; i--){
                printText(window, yLoc, sorted[i].gameName);
                printBar(window, yLoc, sorted[i].count*20.5);
                yLoc+= 50;
            }


            // end the current frame
            window.display();
        }
    }

    return 0;
}
