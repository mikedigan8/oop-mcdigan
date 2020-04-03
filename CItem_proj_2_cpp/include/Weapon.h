#pragma once

#include "CItem.h"

namespace item {
    class Weapon : public CItem {

        public: static const int DEFAULT_BAG_SIZE;
        public: static const int DEFAULT_QUANTITY;

        private: int bagSize;
        private: int quantity;

        public: Weapon(std::string name, int _bagSize = DEFAULT_BAG_SIZE, int _quantity = DEFAULT_QUANTITY);

        public: int getBagSize() const;
        public: void setBagSize(int newSize);

        public: int getQuantity() const;
        public: void setQuantity(int newQuant);

        public: void fire();
    };
}