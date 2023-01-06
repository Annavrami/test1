from flask import Flask, render_template
import os
import random

app = Flask(__name__)


#image

image = ["https://www.google.com/search q=data+scientists&client=ubuntu&hs=Ul&channel=fs&sxsrf=ALiCzsbYo3iVGNh_oCDNhVMDQnumfEIStA:1673008713084&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjCp7KQ-7L8AhXWW_EDHT8wDh0Q_AUoAXoECAEQAw&biw=726&bih=488&dpr=1",
    ,
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
