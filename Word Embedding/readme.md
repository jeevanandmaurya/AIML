# Tiny Word2Vec: C++ to Python

A simple project to see how words turn into math.

### The 3-Step Process

#### 1. The Input (`words.txt`)

You give the engine a few sentences.

* *Example:* "king loves queen", "man loves woman".
* The engine finds which words hang out together.

#### 2. The Engine (`engine.cpp`)

This is the **Math Box**. It does the fast work.

* It gives every word two numbers (coordinates like X and Y).
* It moves "king" and "queen" closer together because they appear in similar spots.
* **Output:** It saves everything into `model.csv`.

#### 3. The Visuals (`main.ipynb`)

This is the **Camera**.

* It reads the `model.csv`.
* It draws a dot for every word on a graph.
* **The Goal:** You should see "King" sitting right next to "Queen" on the map.

---

### 🛠 How to run it

1. **Compile:** Run the C++ cell to turn your code into a tool.
2. **Train:** Run the tool to process your words.
3. **Plot:** Look at the graph to see what the AI learned.

---
