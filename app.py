from sqlite3 import Date
from flask import render_template, url_for, request, redirect
from models import db, Project, app
import datetime



@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/about')
def about_me():
    return render_template('about.html')


@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/projects')
def list_of_projects():
    return render_template('projects.html')


@app.route('/projects/<id>')
def show_detail_of_project(id):
    project = Project.query.get(id)
    individual_skill = project.skills.split(',')
    str_date = str(project.completion_date)
    split_date = str_date.split("-")
    list_of_months = ['Placeholder', 'January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    year = split_date[0]
    month = split_date[1]
    day = split_date[2]
    month_to_int = int(month)
    assign_month = list_of_months[month_to_int]
    readable_date = f'{assign_month} {day}, {year}'
    return render_template('projects.html', project=project, individual_skill=individual_skill,
    readable_date=readable_date)


@app.route('/contact')
def contact_me():
    return render_template('contact.html')


@app.route('/projects/new_project', methods=['GET', 'POST'])
def create_new_project():
    if request.form:
        print(request.form)
        print(request.form['title'])
        split_date = request.form['date'].split('/')
        year = int(split_date[0])
        month = int(split_date[1])
        day = int(split_date[2])
        date_to_submit = datetime.date(year,month,day)
        new_project = Project(title=request.form['title'], completion_date=date_to_submit,
                            description=request.form['desc'], skills=request.form['skills'],
                            github_link=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
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
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')