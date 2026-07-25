# Automated Avatar Debate Agent

This repo contains a framework for creating realistic animated avatars with custom personalities that can debate true crime cases automatically.

## Features
- Opposite personality agents (argumentative vs professional, etc.)
- Knowledge base loading from JSON
- Realistic motion scripting: head turns, gestures, eye contact
- Automated debate loops

## How to Run
```bash
git clone https://github.com/TrueCrimeInvestigates/animated-avatar-debate-agent.git
cd animated-avatar-debate-agent
python3 main.py
```

## Extend It
Add more personalities in the debate_turn method.
Load real case files into the knowledge dict.
Integrate with animation libraries (Three.js, Unity, etc.) for visual avatars.

Verbal command example: "Run the debate between Alex and Jordan on the [case name]"