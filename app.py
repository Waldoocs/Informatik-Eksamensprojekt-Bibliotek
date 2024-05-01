from flask import Flask, render_template
import database

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the books page
@app.route('/Books.html')
def books_html():
    data = database.fetch_data()
    return render_template('Books.html', books=data)

# Route for the books page (alternative URL)
@app.route('/books')
def books():
    data = database.fetch_data()
    return render_template('Books.html', books=data)

if __name__ == '__main__':
    app.run(debug=True)
