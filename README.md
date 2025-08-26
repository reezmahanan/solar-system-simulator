// filepath: README.md
# Animated Solar System Simulator

A beautiful animated solar system simulation built with Python and Pygame, demonstrating object-oriented programming with `__init__` functions.

## Features

- **Realistic planetary orbits** with different speeds
- **Planet trails** showing orbital paths
- **Moon system** (Earth's moon included)
- **Visual effects** including orbital paths and planet labels
- **Smooth animations** at 60 FPS
- **Starry background** for space atmosphere

## Screenshots

![Solar System Animation](screenshot.png)

## Planets Included

- Mercury
- Venus  
- Earth (with Moon)
- Mars
- Jupiter
- Saturn

## Requirements

- Python 3.6+
- Pygame 2.0+

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/solar-system-simulator.git
cd solar-system-simulator
```

2. Install dependencies:
```bash
pip install pygame
```

3. Run the simulation:
```bash
python solar_system.py
```

## Controls

- **Close window** or **ESC** to exit

## Code Structure

The project demonstrates object-oriented programming with:

- `CelestialBody` - Base class for all space objects
- `Planet` - Inherits from CelestialBody, adds orbital mechanics
- `Moon` - Satellite objects that orbit planets
- `SolarSystem` - Main simulation controller

### Key Features of `__init__` Methods

Each class uses `__init__` functions to:
- Initialize object properties
- Set up orbital parameters
- Configure visual attributes
- Establish object relationships

## Customization

You can easily modify:
- Planet colors and sizes
- Orbital speeds and distances  
- Add more planets or moons
- Change visual effects

## License

MIT License - feel free to use and modify!

## Author

Created as a demonstration of Python OOP and Pygame animation.
