#pragma once

#include "CItem.h"

namespace item {
    class Mask : public CItem {
        public: Mask(std::string _name, std::string _properties, bool isOn = false);

        private: const std::string properties;
        private: bool isOn;

        public: bool getIsOn() const;

        public: void putOn();
        public: void takeOff();

        public: std::string getProperties() const;

        public: void stopUsing();

        public: void setCDirection(std::string newDirect);
    };
}