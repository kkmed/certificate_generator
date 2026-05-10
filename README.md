# Certificate Generator & Email Dispatcher 🎓

A fully automated, wizard-driven Python tool designed to bulk-generate high-quality custom image certificates from a CSV file and securely dispatch them via email.

## 🚀 Key Features
- **Dynamic Configuration Wizard:** Set your organization name, event details, dignitaries, and dates securely via an interactive console without modifying any python code.
- **Auto-Persistent Settings:** Configurations are saved to a local JSON file across runs so you only have to specify your university or company details once.
- **Template System:** Swap between multiple certificate designs (`.png` files) seamlessly. The text engine automatically calculates layout and scales fonts dynamically to fit the design.
- **Secure Emailing:** Connects out to Google's SMTP servers securely using environment variables (`.env`) rather than hardcoding passwords in plain-text.
- **CSV Data Processing:** Reads massive lists of recipient names and emails instantly while discarding invalid rows.

## 📂 Project Structure
To keep the root clean, the project follows a strict domain architecture.
```text
certificate_generator/
├── src/                      # Engine source code
├── data/                     # Input files (students.csv) and saved configs
├── templates/                # The blank HD image templates (.png)
├── assets/                   # Fonts used across the engine (.ttf)
├── output/                   # Where the program outputs finished generation bursts
├── .env                      # Locally injected email credentials (git-ignored)
└── requirements.txt          # Python dependencies
```

## ⚙️ Setup & Installation

**1. Clone the repository and install dependencies**
Ensure your terminal is located at the root `certificate_generator/` folder.
```shell
pip install -r requirements.txt
```

**2. Secure your Email Credentials**
To automatically dispatch emails, duplicate or rename `.env.example` to `.env`. Edit the file to include your Google App Password and sender email. (⚠️ Note: Google requires you to enable 2-Step Verification and use an "App Password", not your normal login password).
```env
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_16_digit_app_password
```

**3. Populate the Recipient Data**
Open `data/students.csv`. Ensure you keep the top header line intact (`name,email`). Below that, add the exact names and emails of the people receiving the certificates.

---

## 🏃‍♂️ Running the Engine

Execute the primary script from the root directory:
```shell
python src/main.py
```

### The Workflow:
1. **Initial Setup:** On your very first run (or if you choose Option 4), the interactive wizard will ask you for your University name, event details, and signing dignitaries. 
2. **Execution:** Select whether you want to **1. Generate Certificates**, **2. Send Emails**, or **3. Generate + Send**.
3. **Template Selection:** Select your visual template (e.g., `1`, `2`, or `3`). The engine handles the offset and scaling automatically!
4. **Validation:** Check the auto-generated `output/` folder to see your finalized certificates before deciding to send them out over email.

## 🎨 Customizing Templates
If you wish to add a new visual template design:
1. Drop your new high-resolution `.png` file into the `templates/` folder.
2. Open `src/generator.py` and add a new entry to the `TEMPLATE_CONFIGS` dictionary at the top of the file mapping your new layout coordinates.