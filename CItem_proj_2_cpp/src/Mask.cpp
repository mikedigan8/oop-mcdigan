#include "Mask.h"
#include <iostream>

namespace item {
    bool isOn;
    
    Mask::Mask(std::string _name, std::string _properties, bool _isOn) 
        : CItem(_name), properties(_properties), isOn(_isOn)
    {
        if(!getUsing()) isOn = false;
        else isOn = true;
    }

    bool Mask::getIsOn() const {
        return isOn;
    }

    void Mask::putOn() {
        if(getUsing()) isOn = true;
    }
    void Mask::takeOff() {
        isOn = false;
    }

    std::string Mask::getProperties() const {
        return properties;
    }

    void Mask::stopUsing() {
        CItem::stopUsing();
        isOn = false;
    }

    void Mask::setCDirection(std::string newDirect) {
        bool accept = false;
        for(int i = 0; i < 4; i++) {
            if(newDirect == ACCEPTABLE_DIRECTIONS[i]) accept = true;
        }

        if(!accept) CItem::setCDirection("none");
        else CItem::setCDirection(newDirect);
        if (getCDirection() == "none") stopUsing();
    }
}
