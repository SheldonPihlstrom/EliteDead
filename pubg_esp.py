
import random
import time

class ESPOverlay:
    def __init__(self):
        self.enemies = []

    def scan(self):
        for i in range(10):
            self.enemies.append({
                'id': i,
                'x': random.randint(100, 1200),
                'y': random.randint(100, 800),
                'health': random.randint(1, 100)
            })

    def draw_box(self, enemy):
        print(f"[ESP] Player {enemy['id']}: Box at ({enemy['x']},{enemy['y']}), HP: {enemy['health']}%")

    def update_overlay(self):
        self.scan()
        for enemy in self.enemies:
            self.draw_box(enemy)
            time.sleep(0.2)

    def draw_radar(self):
        print("[ESP] Radar Active")
        for e in self.enemies:
            print(f"Enemy {e['id']} → X: {e['x']//10}, Y: {e['y']//10}")

if __name__ == "__main__":
    overlay = ESPOverlay()
    overlay.update_overlay()
    overlay.draw_radar()
