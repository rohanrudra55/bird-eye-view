# Parking Assist
Parking Assist System Experiments

---
## Using

* Basic intution
* Panaroma logic

## Goals
- [x] Bird eye view with prespective transform in one side
    - [ ] Enchance the results
    - To run:
        - Put folder path in `config.yaml`
        - ``` python3 test.py ```

- [ ] 360 bird eye view of the surrounding using traditional approach
- [x] Steering wheel simulator

---

##### Project Structure
```
├── PASE
│   ├── __init__.py
│   ├── config.yaml
│   ├── main.py
│   ├── processing
│   └── sensors
│       ├── camera
│       │   └── __init__.py
│       ├── streeingwheel
│       │   └── __init__.py
│       └── ultrasonic
│           └── __init__.py
├── SWS
│   ├── main.py
|   ├── data
│   |       └── info.txt
│   └── resources
│       ├── fonts
│       │   └── info.txt
│       ├── images
│       │   └── info.txt
│       └── sounds
│           └── info.txt
├── README.md
├── SWS
├── assets
├── docs
├── requirements.txt
├── setup.py
└── test.py
```
##### On going 
@Maaitrayo: _SWS_ (Steering Wheel Simulation)

@rohanrudra55: _PASE_
