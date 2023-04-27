from flask import Flask, render_template, request, redirect

app = Flask(__name__)

test_bd_response = [(1, "22:00"), (2, "22:00"),
                    (3, "22:00"), (4, "22:00"), (5, "22:00")]


@app.route("/", methods=['POST', 'GET'])
def main_page():
    if request.method == "POST":
        result = request.form
        test_bd_response.append(
            (result["PC"], result["Time"] + " " + result["Comm"]))
        return redirect("/")
    else:
        return render_template("index.html", test_bd_response=test_bd_response)


if __name__ == "__main__":
    app.run(debug=True)
