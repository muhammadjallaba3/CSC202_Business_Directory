from flask import Flask, render_template, request, redirect, url_for
from models import Business, DirectoryManager

app = Flask(__name__)

# Create an instance of our manager to hold the data
manager = DirectoryManager()

# Add a sample business so the page isn't completely empty at first
sample_biz = Business("Kano Tech Hub", "Technology", "Kano City")
manager.add_business(sample_biz)

@app.route('/')
def home():
    # This route handles the Home Page
    recent = manager.get_recently_added()
    return render_template('index.html', businesses=manager.all_businesses, recent=recent)

@app.route('/add', methods=['GET', 'POST'])
def add_business():
    # This route handles the form to add a new business
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        location = request.form.get('location')
        
        # Create a new Business object and add it to our manager
        new_biz = Business(name, category, location)
        manager.add_business(new_biz)
        
        return redirect(url_for('home'))
        
    return render_template('add_business.html')

if __name__ == '__main__':
    app.run(debug=True)