
import time

class Wallhack:
    def __init__(self):
        self.players = [
            {"name": "Player1", "x": 200, "y": 400, "team": "enemy"},
            {"name": "Player2", "x": 500, "y": 320, "team": "ally"},
            {"name": "Player3", "x": 700, "y": 190, "team": "enemy"}
        ]

    def reveal_enemies(self):
        print("[Wallhack] Scanning through walls...")
        for player in self.players:
            if player["team"] == "enemy":
                print(f"Enemy: {player['name']} → X: {player['x']}, Y: {player['y']}")
            time.sleep(0.3)

    def toggle_vision_mode(self):
        print("Thermal vision mode: ON")
        time.sleep(0.5)
        print("X-ray mode: ACTIVE")

if __name__ == "__main__":
    wh = Wallhack()
    wh.reveal_enemies()
    wh.toggle_vision_mode()
