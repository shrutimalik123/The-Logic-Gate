import random

def logic_gate_game():
    # 1. Game Setup
    gates = ["AND", "OR", "XOR"]
    level = 1
    score = 0
    
    print("--- 🔌 THE LOGIC GATE 🔌 ---")
    print("Choose the correct gate to achieve the target output!")
    print("Logic Rules:")
    print(" - AND: Both must be True")
    print(" - OR : At least one must be True")
    print(" - XOR: Exactly one must be True")

    # 2. Game Loop
    while level <= 5:
        in1 = random.choice([True, False])
        in2 = random.choice([True, False])
        
        # Pick a gate and calculate what the correct answer would be
        gate_answer = random.choice(gates)
        
        if gate_answer == "AND": target = in1 and in2
        elif gate_answer == "OR": target = in1 or in2
        else: target = in1 != in2 # XOR logic

        print(f"\n--- LEVEL {level} ---")
        print(f"INPUT A: {in1}")
        print(f"INPUT B: {in2}")
        print(f"GOAL OUTPUT: {target}")
        
        choice = input("Select Gate (AND, OR, XOR): ").upper().strip()

        # 3. Validation Logic
        user_result = False
        if choice == "AND": user_result = in1 and in2
        elif choice == "OR": user_result = in1 or in2
        elif choice == "XOR": user_result = in1 != in2
        else:
            print("⚠️ Invalid Gate! System Short-circuit.")
            continue

        if user_result == target:
            print("✅ CONNECTION ESTABLISHED!")
            score += 10
        else:
            print(f"❌ CONNECTION FAILED! {choice} resulted in {user_result}.")
        
        level += 1

    # 4. End State
    print(f"\n🏁 MISSION COMPLETE | Final Score: {score}/50")
    if score == 50:
        print("🧠 MASTER ARCHITECT: You understand the language of machines perfectly.")

logic_gate_game()
