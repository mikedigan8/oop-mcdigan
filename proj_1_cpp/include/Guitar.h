#pragma once

#include <stdexcept>
#include <string>
#include <array>

namespace instrument {
    class Guitar {
            public: static const int DEFAULT_STRING_COUNT;
            public: static const int DEFAULT_STRING_GAUGE;
            public: static const std::string DEFAULT_TUNING;
            public: static const char ACCEPTABLE_NOTES[7];
            public: static const double DEFAULT_VOLUME;
            private: int stringCount;
            private: int stringGauge;
            private: std::string tuning;
            private: double volume;
            
            public: Guitar(int _stringCount = DEFAULT_STRING_COUNT, int _stringGauge = DEFAULT_STRING_GAUGE, std::string _tuning = DEFAULT_TUNING, double _volume = DEFAULT_VOLUME);

            public: int getStringCount() const;

            public: void setStringCount(int numStrings);

            public: int getStringGauge() const;

            public: void setStringGauge(int gauge);

            public: std::string getTuning() const;

            public: void setTuning(std::string tuning);

            public: double getVolume() const;

            public: void setVolume(double newVol);
    };
}