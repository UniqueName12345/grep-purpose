#pragma once

#include <string>

// Basic representation of a non-player character.
// This will be expanded with needs, relationships, and other state as the project grows.
class NPC {
public:
    NPC(const std::string& name, int age);

    // Simulate the passage of time for this NPC.
    void tick();

    // Get a short description of the NPC's current state.
    std::string describe() const;

private:
    std::string name_;
    int age_;
    int hunger_;   // 0 (full) to 100 (starving)
    int energy_;   // 0 (exhausted) to 100 (well rested)
};
