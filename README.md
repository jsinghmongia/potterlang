# 🪄 PotterLang (.wand)

A Harry Potter-themed interpreted programming language written in Python.

## Installation
bash
pip install potterlang
## Quick Start
Create a file named `spell.wand`:
potter
Accio house_points = 50
Lumos "Evaluating House Points..."
Riddikulus (house_points > 40) {
    Lumos "10 points to Gryffindor!"
} Finite {
    Lumos "Sent to Azkaban!"
}

## Run it from any terminal:
bash
potter spell.wand
