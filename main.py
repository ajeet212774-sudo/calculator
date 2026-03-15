from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    num1 = None
    num2 = None
    operation = None

    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            operation = request.form.get("operation")

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    error = "Division by zero is not allowed."
                else:
                    result = num1 / num2
            else:
                error = "Please select a valid operation."
        except (TypeError, ValueError):
            error = "Please enter valid numbers."

    return render_template(
        "index.html",
        result=result,
        error=error,
        num1=num1,
        num2=num2,
        operation=operation
    )


# ---------- JSON APIs (optional, useful for Postman / frontend) ----------

@app.route("/api/add", methods=["POST"])
def api_add():
    data = request.get_json()
    try:
        num1 = float(data.get("num1"))
        num2 = float(data.get("num2"))
        return jsonify({"operation": "addition", "result": num1 + num2})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400


@app.route("/api/subtract", methods=["POST"])
def api_subtract():
    data = request.get_json()
    try:
        num1 = float(data.get("num1"))
        num2 = float(data.get("num2"))
        return jsonify({"operation": "subtraction", "result": num1 - num2})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400


@app.route("/api/multiply", methods=["POST"])
def api_multiply():
    data = request.get_json()
    try:
        num1 = float(data.get("num1"))
        num2 = float(data.get("num2"))
        return jsonify({"operation": "multiplication", "result": num1 * num2})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

@app.route("/api/divide", methods=["POST"])
def api_divide():
    data = request.get_json()
    try:
        num1 = float(data.get("num1"))
        num2 = float(data.get("num2"))

        if num2 == 0:
            return jsonify({"error": "Division by zero is not allowed."}), 400

        return jsonify({"operation": "division", "result": num1 / num2})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8000,debug=True)
