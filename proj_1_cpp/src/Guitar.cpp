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
        //something here to validate the tuning
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
        //something here to validate the tuning
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