from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about_me():
    return render_template('about.html')


@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/projects/<id>')
def show_detail_of_project():
    return render_template('detail.html')


@app.route('/contact')
def contact_me():
    return render_template('contact.html')

@app.route('/projects/new')
def create_new_project():
    return render_template('add_project.html')


@app.route('/projects/<id>/edit')
def edit_or_update_project():
    return render_template('edit_project.html')

@app.route('/delete/<id>')
def delete_project(id):
    pass
    # pet = Pet.query.get_or_404(id)
    # db.session.delete(pet)
    # db.session.commit()
    # return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')