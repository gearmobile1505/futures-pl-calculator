# Futures P/L Calculator

This project is a simple web application that allows users to calculate potential profit and loss for various futures trading instruments. It provides a user-friendly interface to input trading parameters such as entry price, take profit, and stop loss.

## Features

- Input fields for entry price, take profit, and stop loss.
- Calculation of potential profit and loss based on user inputs.
- Support for micro futures instruments including:
  - MYM!
  - MNQ1
  - MESM2025
  - MGC1!
  - MCL1!
  - MBT1!
  - M6e1!
  - M6A1!

## Requirements

- Python 3.x
- Flask

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/futures-pl-calculator.git
   cd futures-pl-calculator
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Enter the entry price, take profit, and stop loss in the provided fields.
- Select the futures instrument from the dropdown menu.
- Click on the "Calculate" button to see the potential profit and loss for your trade.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.