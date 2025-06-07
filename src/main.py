from npc import NPC
from simulation import Simulation


def main() -> None:
    sim = Simulation()
    player = NPC("Player", 25)
    friend = NPC("Jamie", 28)
    sim.add_npc(player)
    sim.add_npc(friend)

    while True:
        print("\n" + sim.time_str())
        for n in sim.npcs:
            print(n.describe())
        cmd = input("[a]dvance, [t]alk, [e]at, [s]leep, [q]uit > ").strip().lower()
        if cmd == "a":
            sim.tick()
        elif cmd == "t":
            target_name = input("Talk to who? ")
            target = next((n for n in sim.npcs if n.name.lower() == target_name.lower()), None)
            if target and target is not player:
                player.talk_to(target)
                sim.tick()
                print(f"You talked to {target.name}.")
            else:
                print("No such NPC.")
        elif cmd == "e":
            player.eat()
            sim.tick()
        elif cmd == "s":
            player.sleep()
            sim.tick()
        elif cmd == "q":
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
