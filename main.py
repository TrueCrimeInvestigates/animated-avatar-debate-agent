#!/usr/bin/env python3
"""
Automated Avatar Debate Agent Framework
Creates realistic animated avatars with custom personalities
that debate true crime cases with head turns, gestures, eye contact.
"""

import json
import time

class AvatarAgent:
    def __init__(self, name, personality, knowledge_base):
        self.name = name
        self.personality = personality  # e.g. "argumentative", "flirtatious", "unhinged", "professional"
        self.knowledge = knowledge_base
        self.position = "neutral"  # neutral, leaning_left, leaning_right

    def speak(self, message):
        print(f"[{self.name} - {self.personality}] {message}")
        # Simulate motion: head turn toward listener
        self._animate_head_turn("listener")
        time.sleep(0.5)

    def _animate_head_turn(self, direction):
        print(f"  -> {self.name} turns head {direction}, eyes locked, subtle nod")

    def gesture(self, gesture_type):
        print(f"  -> {self.name} {gesture_type}")

    def debate_turn(self, topic, opponent):
        if self.personality == "argumentative":
            self.speak(f"On {topic}, the evidence clearly shows...")
            self.gesture("points finger emphatically")
        elif self.personality == "professional":
            self.speak(f"Let's examine the facts on {topic} objectively.")
            self.gesture("opens palms calmly")
        # Add more personalities as needed

# Example: Two opposite agents debating a true crime case
def run_debate():
    case = "The 1996 murder of JonBenét Ramsey"  # or any case
    
    agent1 = AvatarAgent(
        "Alex", 
        "argumentative", 
        {"belief": "Family cover-up", "evidence": [" ransom note inconsistencies", " pineapple evidence"]}
    )
    agent2 = AvatarAgent(
        "Jordan", 
        "professional", 
        {"belief": "Intruder theory", "evidence": [" basement window", " unidentified DNA"]}
    )
    
    print("=== AUTOMATED AVATAR DEBATE ===")
    print(f"Topic: {case}")
    print(f"Agent 1: {agent1.name} ({agent1.personality})")
    print(f"Agent 2: {agent2.name} ({agent2.personality})")
    print()
    
    for i in range(3):  # 3 rounds
        print(f"--- Round {i+1} ---")
        agent1.debate_turn(case, agent2)
        agent2.debate_turn(case, agent1)
        print()
    
    print("Debate complete. Motions synced to dialogue.")

if __name__ == "__main__":
    run_debate()