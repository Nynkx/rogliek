import tcod

W, H = 80, 60



def main() ->None:
    tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
    console = tcod.Console(W, H, order="F")

    with tcod.context.new(columns=console.width, rows=console.width, tileset=tileset) as context:
        while True:
            console.clear()
            console.print(x=10, y=10, string="Hello world!")
            console.draw_frame(x=0, y=0, width=W, height=H, decoration="╔═╗║ ║╚═╝")
            context.present(console)

            for event in tcod.event.wait():
                context.convert_event(event=event)
                print(event)
                if isinstance(event, tcod.event.Quit):
                    raise(SystemExit)


if __name__ == "__main__":
    main()