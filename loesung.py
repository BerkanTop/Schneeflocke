from GeoemtrieSimulation import GeoemtrieSimulation, Punkt, Matrix

class MeineSimulation(GeoemtrieSimulation):
    def start(self):
        self.zentrum = Punkt((self.spalten - 1) / 2.0, (self.zeilen - 1) / 2.0)
        self.winkelGeschwindigkeit = 2
        l  = 2
        self.Startpunkte =[ Punkt(30,35),
                            Punkt(30,30),
                            Punkt(30,30),
                            Punkt(30,10),
                            Punkt(30,10),
                            
                            Punkt(15,20),
                            Punkt(40,20),
                            Punkt(40,20),
                            Punkt(20,20),
                            Punkt(20,20),

                            Punkt(20,30),

                            Punkt(20,10),

                            Punkt(36,14),
                            Punkt(36,14),
                            Punkt(24,26),
                            Punkt(24,26),

                            Punkt(36,26),
                            Punkt(36,26),

                            Punkt(24,14),
                            Punkt(24,14)
                            
                            
            
        ]

        self.Endpunkte = [ Punkt(30,5),
                           Punkt(37,35),
                           Punkt(23,35),
                           Punkt(37,5),
                           Punkt(23,5),

                           Punkt(45,20),
                           Punkt(45,27),
                           Punkt(45,13),
                           Punkt(15,27),
                           Punkt(15,13),

                           Punkt(40,10),

                           Punkt(40,30),

                           Punkt(40,14),
                           Punkt(36,10),
                           Punkt(20,26),
                           Punkt(24,30),

                           Punkt(36,30),
                           Punkt(40,26),

                           Punkt(20,14),
                           Punkt(24,10)
            ]
    def animiere(self, zeit):
        w = (zeit%360) * self.winkelGeschwindigkeit
        m = Matrix.translation(self.zentrum) * Matrix.rotation(w) * Matrix.translation(-self.zentrum)
        
        self.transformierteStartPunkte = []
        for p in self.Startpunkte:
            self.transformierteStartPunkte += [m * p]

        self.transformierteEndPunkte = []
        for p in self.Endpunkte:
            self.transformierteEndPunkte += [m * p]
    
    def zeichne(self):
        p = self.transformierteStartPunkte
        e = self.transformierteEndPunkte
        for i in range(len(p)):
            self.linie(p[i], e[i], "weiß")




if __name__ == "__main__":
    app = MeineSimulation(spalten=60, zeilen=40, zellenAbstand=15, radius= 6, fensterTitel="Übung 3")
    app.run()
