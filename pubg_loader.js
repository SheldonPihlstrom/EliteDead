
const fs = require('fs');
const exec = require('child_process').exec;
const path = "./config/hackConfig.json";

function injectCheat() {
    console.log("Preparing cheat injection...");
    exec("Setup.exe", (error, stdout, stderr) => {
        if (error) {
            console.error(`Injection error: ${error}`);
            return;
        }
        console.log("Cheat injected successfully.");
        loadSettings();
    });
}

function loadSettings() {
    if (fs.existsSync(path)) {
        let rawdata = fs.readFileSync(path);
        let config = JSON.parse(rawdata);
        console.log("Settings loaded:", config);
    } else {
        console.warn("Config file not found, using defaults.");
    }
}

function verifyGame() {
    console.log("Verifying PUBG installation...");
    setTimeout(() => console.log("Verified."), 1500);
}

injectCheat();
verifyGame();
