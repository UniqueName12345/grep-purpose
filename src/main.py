from npc import NPC
from simulation import Simulation
from io_utils import fprint, finput, cls
from chat_service import ChatService


def log_action(chat_service: ChatService, npc: NPC, action: str) -> None:
    """Generate a log line via Pollinations and append to log.txt."""
    prompt = (
        f"Write one short sentence describing how {npc.name} {action}. "
        f"Stats: hunger {npc.hunger} energy {npc.energy} social {npc.social} money {npc.money}."
    )
    line = chat_service.ask(npc.persona or "Narrator", prompt)
    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(line + "\n")


def main() -> None:
    sim = Simulation()
    chat_service = ChatService()
    player = NPC("Player", 25, "A confused human trying to make sense of life.")
    friend = NPC("Jamie", 28, "A friendly but quirky neighbor who loves trivia.")
    sim.add_npc(player)
    sim.add_npc(friend)

    while True:
        cls()
        fprint(sim.time_str())
        for n in sim.npcs:
            fprint(n.describe())
        cmd = finput("[a]dvance, [t]alk, [e]at, [s]leep, [o]ptions, [q]uit > ").strip().lower()
        if cmd == "a":
            sim.tick()
            log_action(chat_service, player, "watched time pass")
        elif cmd == "t":
            target_name = finput("Talk to who? ")
            target = next((n for n in sim.npcs if n.name.lower() == target_name.lower()), None)
            if target and target is not player:
                question = finput("What do you ask? ")
                player.talk_to(target, question, chat_service)
                sim.tick()
                fprint(f"You talked to {target.name}.")
                log_action(chat_service, target, f"chatted with {player.name}")
            else:
                fprint("No such NPC.")
        elif cmd == "e":
            player.eat()
            sim.tick()
            log_action(chat_service, player, "ate")
        elif cmd == "s":
            player.sleep()
            sim.tick()
            log_action(chat_service, player, "slept")
        elif cmd == "o":
            choice = finput("Use GET API or OpenAI? [g/o] > ").strip().lower()
            if choice == "g":
                chat_service.use_get = True
                fprint("Using GET API.")
            elif choice == "o":
                chat_service.use_get = False
                fprint("Using OpenAI-compatible API.")
            else:
                fprint("Invalid option.")
        elif cmd == "q":
            break
        else:
            fprint("Invalid command.")


if __name__ == "__main__":
    main()
