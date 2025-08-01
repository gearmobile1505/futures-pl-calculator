from flask import Flask, render_template, request

app = Flask(__name__)

MICRO_CONTRACT_SPECS = {
    "MYM": 0.50,      # $0.50 per point
    "MNQ1": 2.00,     # $2.00 per point
    "MESM2025": 5.00, # $5.00 per point
    "MGC1": 10.00,    # $10.00 per point (micro gold)
    "MCL1": 1.00,     # $1.00 per point (micro crude)
    "MBT1": 0.50,     # $0.50 per point (micro bitcoin)
    "M6E1": 1.25,     # $1.25 per point (micro euro)
    "M6A1": 1.00      # $1.00 per point (micro aussie)
}

@app.route("/", methods=["GET", "POST"])
def index():
    profit = None
    loss = None
    profit_loss = None
    if request.method == "POST":
        entry = float(request.form["entry_price"])
        take_profit = float(request.form["take_profit"])
        stop_loss = float(request.form["stop_loss"])
        instrument = request.form["instrument"]
        contracts = int(request.form.get("contracts", 1))
        contract_size = MICRO_CONTRACT_SPECS.get(instrument, 1)

        profit = abs(take_profit - entry) * contract_size * contracts
        loss = abs(entry - stop_loss) * contract_size * contracts
        profit_loss = True

    return render_template("index.html", profit=round(profit, 2) if profit is not None else None,
                           loss=round(loss, 2) if loss is not None else None,
                           profit_loss=profit_loss)

if __name__ == "__main__":
    app.run(debug=True)