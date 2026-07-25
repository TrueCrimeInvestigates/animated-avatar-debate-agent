#!/usr/bin/env python3
"""
Automated Avatar Debate Agent Framework
Carroll County Comet / Delphi case: Holly Eitenmiller & Anthony Greeno
Two opposite personalities debate the public record.
"""

import json
import time

class AvatarAgent:
    def __init__(self, name, personality, knowledge_base):
        self.name = name
        self.personality = personality
        self.knowledge = knowledge_base
        self.position = "neutral"

    def speak(self, message):
        print(f"[{self.name} - {self.personality}] {message}")
        self._animate_head_turn("listener")
        time.sleep(0.5)

    def _animate_head_turn(self, direction):
        print(f"  -> {self.name} turns head {direction}, eyes locked, subtle nod")

    def gesture(self, gesture_type):
        print(f"  -> {self.name} {gesture_type}")

    def debate_turn(self, topic, opponent):
        facts = self.knowledge.get("facts", [])
        if self.personality == "argumentative":
            self.speak(f"On {topic}, the evidence clearly shows {facts[0] if facts else 'the tip came from Holly herself.'}")
            self.gesture("points finger emphatically")
        elif self.personality == "professional":
            self.speak(f"Let's examine the facts on {topic} objectively. {facts[1] if len(facts)>1 else 'Court records show separate but related charges.'}")
            self.gesture("opens palms calmly")

# Carroll County Comet case - May/Nov 2025
def run_debate():
    case = "Carroll County Comet Delphi charges against Holly Eitenmiller and Anthony Greeno - May 2025 investigation, November 2025 charges"
    
    agent1 = AvatarAgent(
        "Alex", 
        "argumentative", 
        {"belief": "Holly set up Greeno and abused her position at The Comet", "facts": ["Holly called the sheriff herself reporting a giant bag of weed at her apartment", "Greeno told police Holly invited him and another man to the Chamber of Commerce building where she had access through her Comet job and said they could take items because it was being sold", "Holly charged with Level 6 felonies theft and maintaining a common nuisance plus false informing and marijuana possession", "Greeno charged with marijuana possession and visiting a common nuisance in a separate but related case"]}
    )
    agent2 = AvatarAgent(
        "Jordan", 
        "professional", 
        {"belief": "Routine drug investigation with no proven newspaper corruption", "facts": ["Delphi Police responded to Holly's tip on May 11 2025 and found Greeno asleep with a small bag of marijuana", "Text messages showed the two had discussed marijuana and THC products days earlier on May 6", "Holly 55 former Comet editor facing two Level 6 felonies and two misdemeanors", "Greeno 39 from Lafayette facing two Class B misdemeanors - no charges against The Comet itself"]}
    )
    
    print("=== AUTOMATED AVATAR DEBATE ===")
    print(f"Topic: {case}")
    print(f"Agent 1: {agent1.name} ({agent1.personality}) - believes Holly abused her Comet position")
    print(f"Agent 2: {agent2.name} ({agent2.personality}) - sees it as routine drug case")
    print()
    
    for i in range(4):  # 4 rounds for deeper debate
        print(f"--- Round {i+1} ---")
        agent1.debate_turn(case, agent2)
        agent2.debate_turn(case, agent1)
        print()
    
    print("Debate complete. Motions synced to dialogue. Public record loaded verbatim.")

if __name__ == "__main__":
    run_debate()