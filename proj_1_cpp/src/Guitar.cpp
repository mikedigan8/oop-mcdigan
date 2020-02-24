#include <stdexcept>
#include "Guitar.h"
#include <iostream>
namespace instrument {
    const int Guitar::DEFAULT_STRING_COUNT = 6;
    const int Guitar::DEFAULT_STRING_GAUGE = 3221;
    const double Guitar::DEFAULT_VOLUME = 0.0;
    const std::string Guitar::DEFAULT_TUNING = "E A D G B E";
    const char Guitar::ACCEPTABLE_NOTES[7] = {'A','B','C','D','E','F','G'};

    Guitar::Guitar(int _stringCount, int _stringGauge, std::string _tuning, double _volume)
        : stringCount(_stringCount), stringGauge(_stringGauge), tuning(_tuning), volume(_volume) 
    {
        bool acceptTuning = true;
        bool notesIn = false;
        char tempStr = ' ';
        int countStr = 0;
        if(stringCount < 0) stringCount = 0;
        if (volume < 0) {
            volume = 0.0;
        }        
        else if(volume > 10) {
            volume = 10.0;
        }
        for(int i = 0; i < tuning.length(); i++) {
            if(tuning[i] != ' ') {
                //the following two switch statements take and sharp or flat notes and check to make sure
                //they are real notes. Since C flat is not a real note, I change it to B, since E sharp
                //is not a real note I change it to F
                //I also decrease the counter on the string so as to not double count any string
                if(tuning[i] == 'b') {
                    countStr--;
                    switch (tuning[i - 1])
                    {
                    case 'C':
                        tempStr = 'B';
                        break;
                    case 'F':
                        tempStr = 'E';
                        break;
                    default:
                        tempStr = tuning[i - 1];
                        break;
                    }
                }
                else if(tuning[i] == '#') {
                    countStr--;
                    switch (tuning[i - 1])
                    {
                        case 'B':
                            tempStr = 'C';
                            break;
                        case 'E':
                            tempStr = 'F';
                            break;
                        default:
                            tempStr = tuning[i - 1];
                            break;
                    }
                }
                else {
                        tempStr = tuning[i];
                }
                for(int j = 0; j < 7; j++) {
                    if(tempStr == ACCEPTABLE_NOTES[j]) notesIn = true;
                }
                if(!notesIn) acceptTuning = false;
                else {
                    notesIn = false;
                    tempStr = ' ';
                    countStr++;
                }
            }
        }
        if(!acceptTuning || countStr != stringCount) {
            tuning = DEFAULT_TUNING;
        }
    }

    int Guitar::getStringCount() const {
        return stringCount;
    }

    void Guitar::setStringCount(int numStrings) {
        if(numStrings < 0) numStrings = 0;
        stringCount = numStrings;
    }

    int Guitar::getStringGauge() const {
        return stringGauge;
    }

    void Guitar::setStringGauge(int gauge) {
        stringGauge = gauge;
    }

    std::string Guitar::getTuning() const {
        return tuning;
    }

    void Guitar::setTuning(std::string newTuning) {
        bool acceptTuning = true;
        bool notesIn = false;
        char tempStr;
        int countStr = 0;
        for(int i = 0; i < newTuning.length(); i++) {
            if(newTuning[i] != ' ') {
                if(newTuning[i] == 'b') {
                    countStr--;
                    switch (newTuning[i - 1])
                    {
                    case 'C':
                        tempStr = 'B';
                        break;
                    case 'F':
                        tempStr = 'E';
                        break;
                    default:
                        tempStr = newTuning[i - 1];
                        break;
                    }
                }
                else if(newTuning[i] == '#') {
                    countStr--;
                    switch (newTuning[i - 1])
                    {
                        case 'B':
                            tempStr = 'C';
                            break;
                        case 'E':
                            tempStr = 'F';
                            break;
                        default:
                            tempStr = newTuning[i - 1];
                            break;
                    }
                }
                else {
                    tempStr = newTuning[i];
                }
                for(int j = 0; j < 7; j++) {
                    if(tempStr == ACCEPTABLE_NOTES[j]) notesIn = true;
                }
                if(!notesIn) acceptTuning = false;
                else {
                    notesIn = false;
                    tempStr = ' ';
                    countStr++;
                }
            }
        }
        if(!acceptTuning || countStr != stringCount) {
            newTuning = DEFAULT_TUNING;
        }
        tuning = newTuning;
    }

    double Guitar::getVolume() const {
        return volume;
    }

    void Guitar::setVolume(double newVol) {
        if (newVol < 0.0) {
            volume = 0.0;
        }
        else if(newVol > 10.0) {
            volume = 10.0;
        }
        else volume = newVol;
    }
}