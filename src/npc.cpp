#include "npc.h"
#include <sstream>
#include <algorithm>

NPC::NPC(const std::string& name, int age)
    : name_(name), age_(age), hunger_(0), energy_(100) {}

void NPC::tick() {
    // Very naive simulation: hunger increases, energy decreases.
    hunger_ = std::min(100, hunger_ + 10);
    energy_ = std::max(0, energy_ - 5);
}

std::string NPC::describe() const {
    std::ostringstream out;
    out << name_ << " (" << age_ << ") - hunger:" << hunger_ << "% energy:" << energy_ << "%";
    return out.str();
}
