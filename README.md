# 🚀 VoxComm – Raspberry Pi Based Walkie-Talkie System

**VoxComm** is a full-duplex voice communication system designed using Raspberry Pi, SIP protocol, and embedded audio interfaces. Built for real-time communication between vehicle drivers and the control room, it's ideal for public transport systems, logistics fleets, and industrial applications.

---

## 🧠 Overview

This project uses:
- 📦 Raspberry Pi as the core processing unit
- 🎤 USB Microphone for audio capture
- 🔊 MAX98357A DAC with a 3W speaker for playback
- 🧲 Push button for triggering SIP-based VoIP call (via API)
- 📡 Linphone SIP stack for voice call handling
- ⚡ Real-time audio streaming using socket programming

---

## 🎯 Features

- ✅ Full-duplex VoIP audio transmission (like a mobile call)
- ✅ API-triggered SIP call using Python requests
- ✅ Durable hardware interface for vehicle deployment
- ✅ Built-in software-based echo suppression and voice clarity
- ✅ Easy to integrate with transport control systems

---

## 🔧 Hardware Used

| Component         | Description                               |
|------------------|-------------------------------------------|
| Raspberry Pi 3B+  | Main processor board                      |
| USB Microphone    | Voice input device                        |
| MAX98357A DAC     | I2S Class D audio amplifier for speaker   |
| 3W Speaker        | Audio output device                       |
| Push Button       | To trigger API call and start communication|
| 5V Power Supply   | For powering the system                   |

---

## 💻 Software Stack

- **Language**: Python 3
- **VoIP Client**: Linphone with SIP credentials
- **Audio Processing**: PyAudio / ALSA
- **Call Trigger**: API (HTTP POST)
- **GPIO / Button Control**: Python GPIO libraries (if physical button used)

---

## 📂 Project Structure

```
/voxcomm
├── main.py                 # Main execution logic
├── call_handler.py         # SIP call integration and status monitoring
├── audio_streamer.py       # USB mic capture and playback logic
├── config.py               # SIP, API, GPIO configuration
├── requirements.txt        # Python dependencies
└── README.md               # Project overview
```

---

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/yourusername/voxcomm.git
cd voxcomm
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the main script:
```bash
python3 main.py
```

---

## 🔐 SIP & API Configuration

Edit `config.py` and add your credentials:

```python
SIP_USER = "sip_user_here"
SIP_PASS = "sip_password_here"
SIP_DOMAIN = "sip_domain_here"

API_URL = "api_url_here"
DID = "your_did_here"
CAPTAIN_EXTEN = "captain_exten_here"
CUSTOMER_EXTEN = "customer_exten_here"
```

---

## 📸 Hardware Setup

- Connect MAX98357A to Pi I2S pins (GPIO18, 19, 21)
- Plug in USB mic
- Connect push button via GPIO or use USB push button
- Run the script and press the button to initiate the call

---

## 📈 Future Improvements

- Voice activity detection (VAD)
- Audio compression for bandwidth optimization
- Touchscreen UI for drivers
- Cloud monitoring & analytics dashboard

---

## 🙋‍♂️ Author

**Jerin Jaison**  
📍 Thrissur, Kerala, India  
🔗 [LinkedIn](https://www.linkedin.com/in/jerin-jaison-63202a1a2)  
📧 jerinjaison17@gmail.com

---

## 📜 License

This project is open-source and available under the MIT License.

---

_Last updated: August 06, 2025_
