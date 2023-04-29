from flask import Flask, render_template, request, redirect
from init_db import broni
import sqlalchemy as sa


engine = sa.create_engine('sqlite:///broni.db')


app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def main_page():
    if request.method == "POST":
        result = request.form
        if "Delete" in result.keys():
            with engine.connect() as conn:
                update_reqst = sa.update(broni).where(
                    broni.c.id == result["Delete"]).values(value="N/A")
                conn.execute(update_reqst)
                conn.commit()
            return redirect("/")
        else:
            result = request.form
            with engine.connect() as conn:
                update_reqst = sa.update(broni).where(
                    broni.c.id == result["PC"]).values(value=f'{result["Time"]} | {result["Comm"]}')
                conn.execute(update_reqst)
                conn.commit()
            return redirect("/")
    else:
        with engine.connect() as conn:
            select_reqst = sa.select(broni).where(broni.c.value != "N/A")
            result = conn.execute(select_reqst)
            rows = result.fetchall()
        return render_template("index.html", rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
