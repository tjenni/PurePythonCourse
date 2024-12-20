from ursina import *

# Erstellen der Ursina-App
app = Ursina()

# Hinzufügen eines Würfels zur Szene
cube = Entity(model='cube', color=color.orange, scale=(2, 2, 2))

camera.position = (0, 0, -10)
camera.rotation = (0, 4, 0)

# Start der Anwendung
app.run()