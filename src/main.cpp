#include "npc.h"
#include <iostream>

int main() {
    NPC npc("Alex", 30);
    for (int day = 0; day < 5; ++day) {
        npc.tick();
        std::cout << npc.describe() << "\n";
    }
    return 0;
}
