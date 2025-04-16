
# 🔐 Advanced Password Strength Meter

A sleek and interactive Streamlit web app that checks the strength of your passwords, provides suggestions to improve them, and even helps you generate strong passwords with custom options.

## 🚀 Features

- ✅ **Real-time password strength evaluation**
- 🧠 **Feedback and suggestions to improve password security**
- 🔒 **Blacklist of common passwords**
- 🔁 **Checks similarity with previously entered passwords**
- 🔧 **Customizable strong password generator**
- 📜 **Session-based password history tracking**
- 🎨 **Custom styled Streamlit UI**

## 🛠️ Technologies Used

- Python
- Streamlit
- Regular Expressions (`re`)
- SequenceMatcher (from `difflib`)
- Python Standard Libraries: `random`, `string`, `datetime`

## 📸 App Preview

![App Screenshot](https://via.placeholder.com/800x400.png?text=Screenshot+Coming+Soon)

## 💡 How It Works

1. Enter a password.
2. The app analyzes:
   - Length
   - Use of uppercase, lowercase, digits, and special characters
   - Presence in common password list
   - Similarity to previously used passwords
3. Receive a strength score (0–5) and improvement tips.
4. Optionally generate strong passwords with custom criteria.

## 🧪 Local Setup

### Prerequisites

- Python 3.7+
- `pip` package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/password-strength-meter.git
cd password-strength-meter

# Install dependencies
pip install streamlit

# Run the app
streamlit run app.py
