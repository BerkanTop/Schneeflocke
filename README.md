# Schneeflocke – Geometrie-Simulation

Dieses Projekt entstand im Rahmen einer Universitätsübung im Bereich der Computergrafik oder Programmierung. Es handelt sich um eine Python-basierte Simulation, die geometrische Formen auf einem diskreten LED-Raster visualisiert und animiert. Im Fokus steht dabei die Implementierung von 2D-Transformationen mittels Matrizenrechnung und Rasterisierungs-Algorithmen.

## Übersicht

Die Anwendung nutzt Pygame, um ein Koordinatensystem darzustellen, in dem Linien und Formen mathematisch berechnet und auf ein Raster übertragen werden. Das Herzstück des Projekts ist die Simulation einer rotierenden Schneeflocke, deren Form durch eine Vielzahl von Liniensegmenten definiert wird, die sich dynamisch um ein Zentrum drehen.

## Features

* **Matrix-Transformationen**: Implementierung einer eigenen `Matrix`-Klasse für Translation und Rotation unter Verwendung von homogenen Koordinaten.
* **Rasterisierungs-Algorithmen**:
    * Eigene Implementierung des Bresenham-Algorithmus zur Linienzeichnung.
    * Methoden zur Darstellung von Kreisen, Rechtecken und Dreiecken auf einem diskreten Gitter.
* **Modulare Architektur**:
    * `Simulation.py`: Basis-Engine für das Pygame-Fenster und das Raster-Handling.
    * `GeoemtrieSimulation.py`: Erweiterung um mathematische Primitiv-Funktionen.
    * `loesung.py`: Spezifische Anwendung und Animationslogik für das Schneeflocken-Muster.
* **Interaktive Anzeige**: Echtzeit-Rendering der Animation mit konfigurierbaren FPS und Gitter-Größen.

## Projektstruktur

* **`Simulation.py`**: Enthält die Basisklasse `Simulation`. Sie verwaltet das Pygame-Fenster, das Farbmanagement sowie den Main-Loop (Update/Draw).
* **`GeoemtrieSimulation.py`**: Definiert die Klassen `Punkt` und `Matrix` für die Vektorgeometrie sowie Methoden zum Zeichnen von Linien, Kreisen und anderen Primitiven.
* **`loesung.py`**: Die konkrete Implementierung der Aufgabe. Hier werden Start- und Endpunkte definiert und über die Zeitmatrix rotiert.

## Installation & Ausführung

### Voraussetzungen

Stellen Sie sicher, dass Python und die Bibliothek `pygame` installiert sind:

```bash
pip install pygame
```

### Start der Simulation

Das Hauptprogramm kann über die Datei `loesung.py` gestartet werden:

```bash
python3 loesung.py
```

## Bedienung

* Das Fenster öffnet sich mit dem Titel "Übung 3".
* Die Schneeflocke rotiert automatisch um den Mittelpunkt des Rasters.
* Mit der **Esc-Taste** oder durch Schließen des Fensters kann die Simulation beendet werden.

## Mathematische Hintergründe

Die Rotation der Punkte erfolgt durch die Kombination mehrerer Matrizen in jedem Frame:
1.  Translation des Punktes in den Ursprung.
2.  Rotation um den berechneten Winkel (zeit * Winkelgeschwindigkeit).
3.  Rück-Translation an die ursprüngliche Position (Zentrum).

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.

---
**Autor**: BerkanTop
**Kontext**: Universitätsprojekt 
