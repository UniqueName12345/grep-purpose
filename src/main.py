from npc import NPC
from simulation import Simulation
from io_utils import fprint, finput


def main() -> None:
    sim = Simulation()
    player = NPC("Player", 25)
    friend = NPC("Jamie", 28)
    sim.add_npc(player)
    sim.add_npc(friend)

    while True:
        fprint("\n" + sim.time_str())
        for n in sim.npcs:
            fprint(n.describe())
        cmd = finput("[a]dvance, [t]alk, [e]at, [s]leep, [q]uit > ").strip().lower()
        if cmd == "a":
            sim.tick()
        elif cmd == "t":
            target_name = finput("Talk to who? ")
            target = next((n for n in sim.npcs if n.name.lower() == target_name.lower()), None)
            if target and target is not player:
                player.talk_to(target)
                sim.tick()
                fprint(f"You talked to {target.name}.")
            else:
                fprint("No such NPC.")
        elif cmd == "e":
            player.eat()
            sim.tick()
        elif cmd == "s":
            player.sleep()
            sim.tick()
        elif cmd == "q":
            break
        else:
            fprint("Invalid command.")


if __name__ == "__main__":
    main()
