from flask import Flask, render_template, request, url_for, redirect
import generator

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        lowCase = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'x', 'y', 'z')
        upCase = (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'X', 'Y', 'Z')
        numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        specialChar = ('£', '$', '&', '(', ')', '*', '+', '[', ']', '@', '#', '^', '-', '_', '!', '?')
        
        pass_len = int(request.form.get("pass_len"))
        lowCase_choice = request.form.get("lowCase_choice")
        upCase_choice = request.form.get("upCase_choice")
        numbers_choice = request.form.get("numbers_choice")
        specialChar_choice = request.form.get("specialChar_choice")

        charGroup = []

        if lowCase_choice in ['Y', 'y']:
            charGroup.append(lowCase)
        if upCase_choice in ['Y', 'y']:
            charGroup.append(upCase)
        if numbers_choice in ['Y', 'y']:
            charGroup.append(numbers)
        if specialChar_choice in ['Y', 'y']:
            charGroup.append(specialChar)

        if charGroup:
            password = generator.Generator(pass_len, charGroup)
        else:
            password = 'None'
        
        return render_template("index.html", password = password)
        
    return render_template('index.html')


# @app.route("/result", methods = ["GET", "POST"])
# def result():
#     return render_template('index.html')


if __name__ == '__main__':
    # app.config['DEBUG'] = True
    app.run(debug=True)
