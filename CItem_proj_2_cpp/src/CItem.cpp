#include "CItem.h"

namespace item {
    const std::string CItem::ACCEPTABLE_DIRECTIONS[4] = {"none", "left", "right", "down"};

    CItem::CItem(std::string _name, bool _acquired, std::string _cApplied, bool _inUse)
        : name(_name), acquired(_acquired), cApplied(_cApplied), inUse(_inUse)
    {
        if(acquired == false) {
            cApplied = "none";
            inUse = false;
        }
        bool accept = false;
        for(int i = 0; i < 4; i++) {
            if(cApplied == ACCEPTABLE_DIRECTIONS[i]) accept = true;
        }
        if(!accept) cApplied = "none";

        if(cApplied == "none") inUse = false;        
    }

    std::string CItem::getName() const{
        return name;
    }

    void CItem::beenAcquired() {
        acquired = true;
    }

    bool CItem::getAcquired() const{
        return acquired;
    }

    std::string CItem::getCDirection() const {
        return cApplied;
    }

    void CItem::setCDirection(std::string newDirect) {
        bool accept = false;
        for(int i = 0; i < 4; i++) {
            if(newDirect == ACCEPTABLE_DIRECTIONS[i]) accept = true;
        }
        if(!accept) cApplied = "none";
        else cApplied = newDirect;
        if(cApplied == "none") inUse = false;
    }

    bool CItem::getUsing() const{
        return inUse;
    }

    void CItem::useItem() {
        bool accept = false;
        for(int i = 0; i < 4; i++) {
            if(cApplied == ACCEPTABLE_DIRECTIONS[i]) accept = true;
        }
        if(accept && acquired && cApplied != "none") inUse = true;
    }

    void CItem::stopUsing() {
        inUse = false;
    }
}