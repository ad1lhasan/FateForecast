🌌 FateForecast: Destiny's Oracle
Welcome to FateForecast, a thrilling web app that peers into the threads of fate to predict passenger survival! Powered by a cunning Decision Tree Classifier and wrapped in a sleek Flask interface, this project transforms raw passenger data into electrifying predictions of life and destiny. Dare to uncover the secrets of survival? 🚢✨
Table of Contents

The Cosmic Vision
Epic Features
The Data Galaxy
Summoning the Oracle
Wielding the Prophecy
The Codex of Creation
Forging the Oracle
Join the Quest
The Oath of Fate

The Cosmic Vision
FateForecast is no mere application—it's a portal to the unknown! Built on the bones of a Decision Tree Classifier, it deciphers the cryptic patterns of survival from a dataset of 500 passengers. With Flask as its mystical engine and a vibrant HTML interface, FateForecast invites you to input passenger details and witness the oracle's verdict: Survived or Lost to Fate. Ready to challenge destiny? 🌠
Epic Features

Prophetic Insights: Enter passenger details—ID, Name, Age, Gender, Class, Seat Type, and Fare—to unveil their fate in a heartbeat!
Astral Interface: A dazzling HTML form guides you through the cosmos, delivering predictions with flair and finesse.
Guardian of Errors: The oracle shields against chaos, gracefully handling invalid inputs or cosmic disruptions.
Encoded Mysteries: Categorical data (Gender, Class, Seat Type) is transformed into numerical runes using LabelEncoder for seamless prophecy.

The Data Galaxy
The heart of FateForecast lies in passenger_survival_dataset.csv, a celestial archive of 500 passenger souls. Each record holds:

Passenger_ID: A unique star in the cosmos.
Name: A mortal alias (encoded as integers for the oracle's sight).
Age: Years under the mortal sky.
Gender: Male (1) or Female (0), a binary constellation.
Class: Economy, Business, or First (encoded as integers).
Seat_Type: Window, Middle, or Aisle (encoded as integers).
Fare_Paid: The coin paid for passage.
Survival_Status: 1 (Blessed by Survival) or 0 (Claimed by Fate).

The dataset is transmuted into dependent_feature.csv after encoding, ready for the oracle's gaze.
Summoning the Oracle
To awaken FateForecast, follow these sacred rites:

Claim the Codex:
git clone https://github.com/ad1lhasan/FateForecast.git
cd FateForecast


Craft the Sanctum (optional but wise):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Gather the Runes:Ensure Python 3.11+ is your blade. Install the sacred dependencies:
pip install flask numpy pandas scikit-learn seaborn pickle5


Secure the Artifacts:

Place passenger_survival_dataset.csv and model.pkl in the project’s altar.
Or, forge a new model.pkl by channeling the passenger_survival.ipynb ritual.



Wielding the Prophecy

Ignite the Oracle:
python model.py

The portal opens at http://127.0.0.1:5000.

Commune with Fate:

Journey to http://127.0.0.1:5000 in your browser.
Offer passenger details in the cosmic form and submit to receive the prophecy.


A Glimpse of Destiny:

Input: Passenger_ID: 1, Name: 0, Age: 52, Gender: 1, Class: 1, Seat_Type: 2, Fare_Paid: 822.34
Prophecy: "Survival Prediction: Did Not Survive" or "Survived"!



The Codex of Creation
FateForecast/
│
├── model.py                    # The Flask spell that summons the web portal
├── passenger_survival.ipynb    # The sacred scroll for data alchemy and oracle forging
├── passenger_survival_dataset.csv  # The raw cosmic ledger of passenger fates
├── dependent_feature.csv       # The encoded star map of features
├── model.pkl                   # The oracle’s crystallized wisdom
├── templates/
│   └── index.html              # The astral canvas for mortal interaction
└── README.md                   # The tome you now hold

Forging the Oracle
The passenger_survival.ipynb is the crucible where the oracle is born:

Gathering the Stars: Load passenger_survival_dataset.csv with pandas.
Transmuting the Elements: Encode categorical columns (Name, Gender, Class, Seat_Type) with LabelEncoder.
Dividing the Cosmos: Split data into training (80%) and testing (20%) realms.
Crafting the Oracle: Train a DecisionTreeClassifier, achieving ~56% accuracy on the test set.
Sealing the Prophecy: Preserve the oracle as model.pkl with pickle.

To reforge the oracle, chant the notebook’s cells in sequence. Ensure dependencies (numpy, pandas, scikit-learn, seaborn) are invoked.
Join the Quest
Seek to shape the future of FateForecast? Brave souls are welcome!

Fork the repository.
Carve a new branch (git checkout -b epic-quest).
Weave your magic and commit (git commit -m "Unveiled new prophecy").
Push to the stars (git push origin epic-quest).
Summon a Pull Request.

Craft your code in the spirit of PEP 8 and include tests to honor the oracle’s precision.

The Oath of Fate
FateForecast is bound by the MIT License, a pact of freedom and creation. Seek the LICENSE file for the full covenant.

Embark on the journey. Let FateForecast guide your path through the stars! 🌟
