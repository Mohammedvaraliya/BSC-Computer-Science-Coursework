## Practical 07

## Problem Statement

Create Snowfall Particle effect in Unity

---

**The steps to perform snowfall particle effect in Unity:**

1. Create a 2D Unity project.
2. Add a Particle System to your scene and rename it to "Snow."
3. Configure the "Snow" particle system:
    1. Set the shape to a box to define the snowfall area.
    2. Adjust the emission rate to around 100 particles per second.
4. Configure the Lifetime:
    1. Create a custom curve that starts at the bottom, rises up, and falls back down.
5. Adjust the Size:
    1. Set "Size over Lifetime" to "Random Between Two Constants" with values 0.05 and 0.2 to vary particle size.
6. Configure Velocity:
    1. Ensure the particles fall from top to bottom. Set the Y-axis velocity to a negative value.
7. Add Noise:
    1. Apply a Noise Module with a strength of 0.2 to add randomness to particle movement.