from npc import NPC


def main() -> None:
    npc = NPC("Alex", 30)
    for _ in range(5):
        npc.tick()
        print(npc.describe())


if __name__ == "__main__":
    main()
