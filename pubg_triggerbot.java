
public class TriggerBot {
    private static int frame = 0;

    public static void main(String[] args) {
        System.out.println("TriggerBot initialized...");
        while (frame < 20) {
            if (detectEnemy()) {
                fireWeapon();
            } else {
                System.out.println("No enemy detected on frame: " + frame);
            }
            frame++;
            delay();
        }
    }

    public static boolean detectEnemy() {
        return Math.random() > 0.6;
    }

    public static void fireWeapon() {
        System.out.println("Enemy detected - Firing weapon!");
    }

    public static void delay() {
        try {
            Thread.sleep(300);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
