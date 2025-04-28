
import time
import math

class NoRecoil:
    def __init__(self):
        self.pattern = [(-1, 3), (0, 2), (1, 1), (1, -1), (0, -2), (-1, -3)]

    def stabilize_weapon(self):
        print("No Recoil: Stabilizing aim...")
        for i in range(20):
            dx, dy = self.pattern[i % len(self.pattern)]
            print(f"Frame {i}: Correction → ΔX: {dx}, ΔY: {dy}")
            time.sleep(0.1)

    def simulate_weapon_fire(self):
        print("Firing weapon...")
        for _ in range(5):
            print("Bang!")
            time.sleep(0.2)

if __name__ == "__main__":
    stabilizer = NoRecoil()
    stabilizer.simulate_weapon_fire()
    stabilizer.stabilize_weapon()
