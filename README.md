# 🔌 The Logic Gate - Boolean Architecture Sim

A puzzle game that challenges your understanding of Boolean logic—the foundation of all modern computing. You are presented with two binary inputs and a target output; your goal is to select the correct logic gate (AND, OR, or XOR) to complete the circuit. Master these gates, and you master the language of the machine.

This project focuses on teaching:
* **Boolean Operators:** Practical application of `and`, `or`, and the logic of `XOR`.
* **Truth Tables:** Understanding how different inputs result in specific outputs.
* **Conditional Evaluation:** Comparing user-selected logic against a pre-calculated target.
* **Input Normalization:** Ensuring robust string handling for user commands.

---

## ✨ Features

* **Procedural Levels:** Every round generates a new combination of True/False inputs and goal states.
* **Three Core Gates:**
    * **AND:** Output is True only if *both* inputs are True.
    * **OR:** Output is True if *at least one* input is True.
    * **XOR:** Output is True only if the inputs are *different*.
* **Scoring System:** Tracks your performance across 5 levels of increasing complexity.
* **Error Handling:** Protects the game state from invalid gate entries.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `logic_gate.py`.
2.  **Open Terminal:** Navigate to your project folder.
3.  **Run the Script:**
    ```bash
    python logic_gate.py
    ```

### 3. Gameplay Instructions
1.  **Analyze the Inputs:** Check if Input A and Input B are True or False.
2.  **Determine the Goal:** Look at the Goal Output.
3.  **Select a Gate:** Type `AND`, `OR`, or `XOR` to try and match that output.
4.  **Advance:** Complete all 5 levels to be crowned a Master Architect.



---

## 🧠 Code Structure Highlights

### The XOR Shortcut
While Python has built-in `and` and `or`, it doesn't have a keyword for XOR in the same way. However, since XOR is only True when the inputs are different, we can use the "Not Equal" operator as a perfect logical substitute.

```python
# The logic of XOR: True if inputs are different
result = (in1 != in2)

