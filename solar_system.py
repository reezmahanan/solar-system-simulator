import pygame
import math
import random

class CelestialBody:
    def __init__(self, name, x, y, radius, color, mass=1):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.trail = []
        self.max_trail_length = 100

class Planet(CelestialBody):
    def __init__(self, name, distance_from_sun, radius, color, orbital_speed, mass=1):
        super().__init__(name, 0, 0, radius, color, mass)
        self.distance_from_sun = distance_from_sun
        self.orbital_speed = orbital_speed
        self.angle = random.uniform(0, 2 * math.pi)
        self.moons = []
    
    def update_position(self, center_x, center_y):
        self.angle += self.orbital_speed
        self.x = center_x + self.distance_from_sun * math.cos(self.angle)
        self.y = center_y + self.distance_from_sun * math.sin(self.angle)
        
        # Update trail
        self.trail.append((int(self.x), int(self.y)))
        if len(self.trail) > self.max_trail_length:
            self.trail.pop(0)
        
        # Update moons
        for moon in self.moons:
            moon.update_position(self.x, self.y)
    
    def add_moon(self, moon):
        self.moons.append(moon)

class Moon(CelestialBody):
    def __init__(self, name, distance_from_planet, radius, color, orbital_speed):
        super().__init__(name, 0, 0, radius, color)
        self.distance_from_planet = distance_from_planet
        self.orbital_speed = orbital_speed
        self.angle = 0
    
    def update_position(self, planet_x, planet_y):
        self.angle += self.orbital_speed
        self.x = planet_x + self.distance_from_planet * math.cos(self.angle)
        self.y = planet_y + self.distance_from_planet * math.sin(self.angle)

class SolarSystem:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Animated Solar System")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Sun
        self.sun = CelestialBody("Sun", width//2, height//2, 30, (255, 255, 0))
        
        # Create planets
        self.planets = []
        self.create_planets()
        
        # Font for labels
        self.font = pygame.font.Font(None, 24)
    
    def create_planets(self):
        # Mercury
        mercury = Planet("Mercury", 80, 4, (169, 169, 169), 0.04)
        
        # Venus
        venus = Planet("Venus", 110, 6, (255, 198, 73), 0.035)
        
        # Earth
        earth = Planet("Earth", 150, 8, (100, 149, 237), 0.03)
        earth_moon = Moon("Moon", 20, 2, (192, 192, 192), 0.1)
        earth.add_moon(earth_moon)
        
        # Mars
        mars = Planet("Mars", 190, 6, (205, 92, 92), 0.025)
        
        # Jupiter
        jupiter = Planet("Jupiter", 280, 20, (255, 140, 0), 0.015)
        
        # Saturn
        saturn = Planet("Saturn", 350, 16, (238, 203, 173), 0.01)
        
        self.planets = [mercury, venus, earth, mars, jupiter, saturn]
    
    def draw_trail(self, trail, color):
        if len(trail) > 1:
            for i in range(1, len(trail)):
                alpha = i / len(trail)
                trail_color = tuple(int(c * alpha) for c in color)
                pygame.draw.circle(self.screen, trail_color, trail[i], 1)
    
    def draw(self):
        self.screen.fill((0, 0, 20))  # Dark space background
        
        # Draw stars
        for _ in range(100):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            pygame.draw.circle(self.screen, (255, 255, 255), (x, y), 1)
        
        # Draw sun
        pygame.draw.circle(self.screen, self.sun.color, 
                          (int(self.sun.x), int(self.sun.y)), self.sun.radius)
        
        # Draw sun glow effect
        for i in range(5):
            glow_color = (255, 255, 100, 50 - i * 10)
            glow_radius = self.sun.radius + i * 3
        
        # Draw planets and their trails
        for planet in self.planets:
            # Draw orbital path
            pygame.draw.circle(self.screen, (50, 50, 50), 
                             (self.width//2, self.height//2), 
                             int(planet.distance_from_sun), 1)
            
            # Draw trail
            self.draw_trail(planet.trail, planet.color)
            
            # Draw planet
            pygame.draw.circle(self.screen, planet.color, 
                             (int(planet.x), int(planet.y)), planet.radius)
            
            # Draw moons
            for moon in planet.moons:
                pygame.draw.circle(self.screen, moon.color,
                                 (int(moon.x), int(moon.y)), moon.radius)
            
            # Draw planet name
            text = self.font.render(planet.name, True, (255, 255, 255))
            self.screen.blit(text, (planet.x + planet.radius + 5, planet.y - 10))
    
    def update(self):
        for planet in self.planets:
            planet.update_position(self.sun.x, self.sun.y)
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()

if __name__ == "__main__":
    solar_system = SolarSystem(1200, 800)
    solar_system.run()