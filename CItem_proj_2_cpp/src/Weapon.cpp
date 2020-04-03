#include "Weapon.h"

namespace item {
    const int Weapon::DEFAULT_BAG_SIZE = 20;
    const int Weapon::DEFAULT_QUANTITY = 0;

    Weapon::Weapon(std::string _name, int _bagSize, int _quantity)
        : CItem(_name), bagSize(_bagSize), quantity(_quantity)
    {
        if(quantity > bagSize) quantity = bagSize;
    }

    int Weapon::getBagSize() const{
        return bagSize;
    }
    void Weapon::setBagSize(int newSize) {
        bagSize = newSize;
    }

    int Weapon::getQuantity() const{
        return quantity;
    }
    void Weapon::setQuantity(int newQuant) {
        if(quantity + newQuant > bagSize) quantity = bagSize;
        else quantity += newQuant;
    }

    void Weapon::fire() {
        if(quantity > 0 && getUsing()) quantity--;
    }
}