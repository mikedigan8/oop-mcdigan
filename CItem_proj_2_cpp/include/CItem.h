#pragma once

#include <string>
#include <array>

namespace item {
    class CItem {
        public: static const std::string ACCEPTABLE_DIRECTIONS[4];

        private: const std::string name;
        private: bool acquired;
        private: std::string cApplied;
        private: bool inUse;

        public: CItem(std::string _name, bool _acquired = false, std::string _cApplied = "none", bool _inUse = false);

        public: std::string getName() const;

        public: void beenAcquired();

        public: bool getAcquired() const;

        public: std::string getCDirection() const;

        public: void setCDirection(std::string newDirect);

        public: bool getUsing() const;

        public: void useItem();

        public: void stopUsing();
    };
}