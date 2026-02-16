import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the data
try:
    df = pd.read_csv('model.csv')
except FileNotFoundError:
    print("Error: 'model.csv' not found. Run the C++ trainer first!")
    exit()

words = df['word'].values
coords = df[['x', 'y']].values
word_to_vec = dict(zip(words, coords))

# 2. Visualize the Grid
plt.figure(figsize=(10, 8)) # Made figure slightly wider
plt.scatter(df['x'], df['y'], c='blue', alpha=0.6) # Added color and transparency

# Annotate words
for i, txt in enumerate(words):
    plt.annotate(txt, (df['x'][i], df['y'][i]), xytext=(5, 5), textcoords='offset points')

# Draw the Origin Lines
plt.axhline(0, color='grey', linewidth=0.8, linestyle='--')
plt.axvline(0, color='grey', linewidth=0.8, linestyle='--')

# --- NEW: Add Axis Labels ---
# We treat X as the Gender spectrum and Y as the Age spectrum
plt.xlabel("Gender Dimension (Masculine <---> Feminine)", fontsize=12, fontweight='bold', color='darkred')
plt.ylabel("Age Dimension (Young <---> Old)", fontsize=12, fontweight='bold', color='darkblue')

plt.title("C++ Trained Word Map (Concept Visualization)")
plt.grid(True, linestyle=':', alpha=0.6) # Added a light grid for readability
plt.show()

# 3. The Word Math Test: King - Man + Woman = ?
if 'king' in word_to_vec and 'man' in word_to_vec and 'woman' in word_to_vec:
    target_vec = word_to_vec['king'] - word_to_vec['man'] + word_to_vec['woman']

    # Find the word closest to this new vector
    def find_closest(target, word_dict):
        closest_word = None
        min_dist = float('inf')
        for word, vec in word_dict.items():
            # Skip the input words themselves so we don't just find "King" again
            if np.array_equal(vec, word_to_vec['king']) or \
               np.array_equal(vec, word_to_vec['man']) or \
               np.array_equal(vec, word_to_vec['woman']):
                continue

            dist = np.linalg.norm(vec - target)
            if dist < min_dist:
                min_dist = dist
                closest_word = word
        return closest_word

    result = find_closest(target_vec, word_to_vec)
    print(f"Analogy Result: King - Man + Woman = {result}")
else:
    print("One of the required words (king, man, woman) is missing from the dataset.")