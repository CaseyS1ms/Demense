# Demense 

An agent-based sandbox simulation of a medieval kingdom built in Python.
The simulation models individual agents — peasants and merchants — each
following simple rules that produce realistic kingdom-level behaviour
such as population growth, food scarcity, and price fluctuations.

## Overview

The world is procedurally generated using Perlin noise, producing a 
unique map of terrain tiles — farmland, forests, hills, water, and 
mountains. Agents navigate this terrain 
using A* pathfinding, avoiding impassable obstacles to reach farms, 
markets, and other locations.

The simulation is built around three interlocking systems. Agent-based
modelling gives each individual their own properties and behaviour.
Logistic-like population growth emerges naturally from agents competing
for resources. Supply and demand causes food prices to fluctuate based
on scarcity without any manual intervention.

## Features

- Procedural map generation via Perlin noise
- Agent-based modelling with Peasant and Merchant agent types
- Emergent supply and demand economy
- A* pathfinding with route caching for performance
- Real-time visualisation via pygame

## Libraries

- pygame — map and agent rendering
- numpy — efficient grid storage and numerical calculations
- noise — Perlin noise map generation
- matplotlib — live data graphs

## Running the Simulation

*Instructions to be added.*

## Roadmap

[Roadmap.png](Roadmap.png)