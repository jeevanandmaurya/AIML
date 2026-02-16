#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <unordered_map>
#include <cmath>

using namespace std;

int main()
{
    vector<string> words;

    // Read from file
    ifstream input_file("words.txt");
    if (!input_file.is_open())
    {
        cerr << "Error opening file!" << endl;
        return 1;
    }

    string word;
    while (input_file >> word)
    {
        words.push_back(word);
    }
    int word_count = words.size();

    unordered_map<string, int> vocab;

    int index = 0;
    for (size_t i = 0; i < word_count; i++)
    {
        if (vocab.find(words[i]) == vocab.end())
        {
            vocab[words[i]] = index++;
        }
    }
    int vocab_size = vocab.size();

    int embedding_dim = 2;
    vector<vector<float>> vec2d(vocab_size, vector<float>(embedding_dim, 0.0));
    for (int i = 0; i < vocab_size; i++)
    {

        vec2d[i][0] = (rand() % 2000 - 1000) / 1000.0; // Random between -1 and 1
        vec2d[i][1] = (rand() % 2000 - 1000) / 1000.0; // Random between -1 and 1
        cout << words[i] << ": " << vec2d[i][0] << ", " << vec2d[i][1] << endl;
    }

    float learn_rate = 0.01;
    float decay = 0.99;
    int epochs = 2000;

    for (int e = 0; e < epochs; e++)
    {
        for (int j = 0; j < word_count; j+=2)
        {
            int idx1 = vocab[words[j]];
            int idx2 = vocab[words[j + 1]];
            int random_idx = rand() % vocab_size;

            for (int k = 0; k < embedding_dim; k++)
            {
                float error = vec2d[idx2][k] - vec2d[idx1][k];
               

                vec2d[idx1][k] += learn_rate *error;// Move idx1 towards idx2
                vec2d[idx2][k] -= learn_rate * error;// Move idx2 towards idx1

                if (random_idx != idx1 && random_idx != idx2)
                {
                    // Calculate vector from idx1 to random_idx
                   error = vec2d[random_idx][k] - vec2d[idx1][k];
                   
                   vec2d[idx1][k] -= learn_rate * error;// Move idx1 away from random_idx
                }
            }
        }
        learn_rate *= decay;
    }

    // Output for your Python Visualizer
    ofstream output_file("model.csv");
    output_file << "word,x,y" << endl;
    for (auto &pair : vocab)
    {
        string word = pair.first;
        int index = pair.second;
        output_file << word << "," << vec2d[index][0] << "," << vec2d[index][1] << endl;
    }
    output_file.close();

    return 0;
}