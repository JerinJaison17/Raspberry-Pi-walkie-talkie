import lgpio
import time
import subprocess
import requests

# Configuration
BUTTON_PIN = 17  # GPIO pin for push button
API_ENDPOINT = "http://34.100.214.215/driver.php"
PAYLOAD = {
    "did": "4843540700",
    "captainexten": "6674",
    "customerexten": "777"
}
SIP_URI = "sip:6674@sipserver.com"  # Replace with actual SIP URI

# Initialize GPIO
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_input(h, BUTTON_PIN, lgpio.SET_PULL_UP)

# Call state variables
call_active = False
button_prev_state = 1  # Not pressed
linphone_process = None

def call_api():
    try:
        print("Calling API...")
        response = requests.post(API_ENDPOINT, json=PAYLOAD)
        if response.status_code == 200:
            print("API Success!")
            return True
        else:
            print(f"API Failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"API Error: {e}")
        return False

def start_voip_call():
    global linphone_process
    print("Starting VoIP Call...")
    linphone_process = subprocess.Popen(
        ["linphonec"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    time.sleep(2)
    linphone_process.stdin.write(f"call {SIP_URI}\n")
    linphone_process.stdin.flush()

def end_voip_call():
    global linphone_process
    if linphone_process:
        print("Ending Call...")
        linphone_process.stdin.write("terminate\n")
        linphone_process.stdin.flush()
        time.sleep(1)
        linphone_process.terminate()
        linphone_process = None

print("System Ready: Waiting for button press...")

try:
    while True:
        button_state = lgpio.gpio_read(h, BUTTON_PIN)

        # Detect falling edge: button press
        if button_prev_state == 1 and button_state == 0:
            print("Button Press Detected")

            if call_api():
                if not call_active:
                    start_voip_call()
                    call_active = True
                else:
                    end_voip_call()
                    call_active = False

        button_prev_state = button_state
        time.sleep(0.05)  # Polling delay

except KeyboardInterrupt:
    print("Interrupted, exiting...")

finally:
    end_voip_call()
    lgpio.gpiochip_close(h)
