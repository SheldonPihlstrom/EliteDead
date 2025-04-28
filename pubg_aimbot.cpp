
#include <iostream>
#include <vector>
#include <cmath>
#include <thread>
#include <chrono>

struct Target {
    float x, y, distance;
    bool visible;
};

class Aimbot {
public:
    void scanTargets(const std::vector<Target>& targets) {
        for (const auto& target : targets) {
            if (target.distance < 150.0f && target.visible) {
                aimAt(target.x, target.y);
            }
        }
    }

    void aimAt(float x, float y) {
        std::cout << "Aiming at target: (" << x << ", " << y << ")" << std::endl;
        adjustMouse(x, y);
    }

    void adjustMouse(float x, float y) {
        std::this_thread::sleep_for(std::chrono::milliseconds(5));
        std::cout << "Mouse moved to: " << x << ", " << y << std::endl;
    }

    void simulateRecoilControl() {
        for (int i = 0; i < 10; ++i) {
            std::cout << "Recoil compensation frame: " << i << std::endl;
            std::this_thread::sleep_for(std::chrono::milliseconds(10));
        }
    }
};

int main() {
    std::vector<Target> detected = {{100, 200, 120, true}, {150, 50, 180, false}, {90, 60, 80, true}};
    Aimbot bot;
    bot.scanTargets(detected);
    bot.simulateRecoilControl();
    return 0;
}
