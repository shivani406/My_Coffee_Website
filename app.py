from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route: Login Page
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        return redirect(url_for('menu'))
    return render_template('main.html')

# Route: Our Menu Page
@app.route('/menu')
def menu():
    return render_template('menu.html')

# Route: Cart + Place Order (Combined)
@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        # After clicking "Place Order", go to thank you page
        return redirect(url_for('thankyou'))
    return render_template('cart.html')

# Route: Thank You Page
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

# ✅ New Route: Our Story Page
@app.route('/our_story')
def our_story():
    return render_template('our_story.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
