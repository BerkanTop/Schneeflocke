import traceback
import pygame as pg

class Simulation:
    def __init__(
        self,
        spalten=30,
        zeilen=20,
        fps=30,
        zellenAbstand=24,
        radius=10,
        randX=40,
        randY=40,
        hintergrund=(18, 18, 18),
        standardFarbe=(60, 60, 60),
        fensterTitel="LED-Simulation",
    ):
        self.zeilen = zeilen
        self.spalten = spalten
        self.fps = fps

        self.zellenAbstand = zellenAbstand
        self.radius = radius
        self.hintergrund = hintergrund
        self.standardFarbe = standardFarbe

        self.randX = randX
        self.randY = randY
        self.fensterTitel = fensterTitel

        self.breite = 2 * self.randX + self.spalten * self.zellenAbstand
        self.hoehe = 2 * self.randY + self.zeilen * self.zellenAbstand

        self.farben = {
            "schwarz": (0, 0, 0),
            "weiß": (255, 255, 255),
            "weiss": (255, 255, 255),
            "rot": (220, 50, 47),
            "gruen": (133, 153, 0),
            "grün": (133, 153, 0),
            "blau": (38, 139, 210),
            "gelb": (181, 137, 0),
            "magenta": (211, 54, 130),
            "cyan": (42, 161, 152),
            "orange": (255, 128, 0),
            "lila": (108, 113, 196),
            "grau": (100, 100, 100),
            "pink": (255, 105, 180),
            "hintergrund": self.hintergrund,
            "standardfarbe": self.standardFarbe,
        }

        self.grid = []
        self.resetGrid()

        self.zeit = 0

    def start(self):
        pass

    def animiere(self, zeit):
        pass
    
    def zeichne(self, zeit):
        pass

    def setze(self, x, y, farbe):
        if not (0 <= x < self.spalten and 0 <= y < self.zeilen):
            return
        self.grid[y][x] = self._resolveFarbe(farbe)

    def resetGrid(self):
        self.grid = [
            [self.standardFarbe for _ in range(self.spalten)]
            for _ in range(self.zeilen)
        ]

    def run(self):
        pg.init()
        screen = pg.display.set_mode((self.breite, self.hoehe))
        pg.display.set_caption(self.fensterTitel)
        clock = pg.time.Clock()

        self.resetGrid()
        self.zeit = 0

        try:
            self.start()

            running = True
            while running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                    elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                        running = False

                clock.tick(self.fps)

                self.resetGrid()
                self.animiere(self.zeit)
                self.zeichne()
                self.zeit += 1

                screen.fill(self.hintergrund)
                for y in range(self.zeilen):
                    for x in range(self.spalten):
                        cx = self.randX + x * self.zellenAbstand + self.zellenAbstand // 2
                        cy = self.randY + y * self.zellenAbstand + self.zellenAbstand // 2
                        pg.draw.circle(screen, self.grid[y][x], (cx, cy), self.radius)

                pg.display.flip()

        except Exception:
            traceback.print_exc()
        finally:
            pg.quit()

    def _resolveFarbe(self, f):
        if isinstance(f, tuple):
            if len(f) != 3:
                raise ValueError(f"RGB-Tuple muss 3 Werte haben, erhalten: {f!r}")
            r, g, b = f
            return (int(r), int(g), int(b))

        if isinstance(f, str):
            key = f.strip().lower()
            if key in self.farben:
                return self.farben[key]

        raise ValueError(
            f"Unbekannte Farbe: {f!r}. Nutze {list(self.farben.keys())} oder (R,G,B)."
        )