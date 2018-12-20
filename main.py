def run():
    from function.Player import create_player, display_all
    for i in range(2):
        create_player("player{}".format(i), "elf", "voleur")
    display_all()


if __name__ == "__main__":
    run()
