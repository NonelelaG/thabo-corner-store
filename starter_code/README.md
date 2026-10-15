# Thabo's Corner Store — Sales Insights System

**Student:** Nonelela Gadu
**Modules:** KM-04 (Data & Databases) + KM-05 (Programming & Python)
**Qualification:** Occupational Certificate — AI Software Developer (NQF 4)

An integrated project that takes messy corner-shop sales data, cleans it,
stores it in a relational database, analyses it in Python, visualises the
results as charts, and protects the reports behind a password gate.

---

## 1. How to install and run

**Requirements:** Python 3.10+, `pip`, and the packages in
`requirements.txt`.

```bash
# Clone the repository
git clone https://github.com/NonelelaG/thabo-corner-store.git
cd "thabo-corner-store"

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate         # Windows
# source venv/bin/activate    # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Run the project
cd starter_code
python main.py