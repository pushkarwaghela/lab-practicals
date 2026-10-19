# BE (E&C) Lab Practice I - DSV and IoT practicals

Amrutvahini College of Engineering, Sangamner - SPPU 2019 course, Semester VII (410346).

## Layout
| Folder | Contents |
|---|---|
| `dsv/` | `DSV_Practicals_1_to_10.py` - all 10 Data Science & Visualization practicals (one `# %%` cell each) |
| `iot/arduino/` | Arduino sketches for Experiments 1-6 (open each `.ino` in the Arduino IDE) |
| `iot/raspberrypi/` | Python scripts for Experiments 8-11 |
| `docs/` | Study guides (steps, wiring, theory, viva questions) as PDF |

## DSV quick start
```bash
cd dsv
pip install -r requirements.txt
jupyter notebook          # or: python DSV_Practicals_1_to_10.py
```
Datasets (`diabetes.csv`, `train.csv`/`titanic.csv`, `your_dataset.csv`) go in the `dsv/` folder; the script downloads or generates them if missing.

## IoT quick start
- Arduino: open `iot/arduino/expXX_name/expXX_name.ino`, choose Tools > Board > Arduino Uno and the COM port, then Upload.
- Raspberry Pi: `python3 iot/raspberrypi/exp08_gpio_led_blink.py` (Pi 5: `pip install rpi-lgpio`).
- Experiment 11 runs in simulation mode on a laptop: `pip install flask && python exp11_smart_home.py`, then open http://localhost:5000.

## Status
- DSV practicals 1-10: run end to end.
- Arduino sketches: not tested on hardware - check pins against your kit.
- Raspberry Pi scripts: syntax checked; Experiment 11 tested in simulation mode.
