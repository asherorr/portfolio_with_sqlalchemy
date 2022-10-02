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
    projects = Project.query.all()
    return render_template('about.html', projects=projects)


@app.route('/skills')
def skills():
    projects = Project.query.all()
    return render_template('skills.html', projects=projects)


@app.route('/projects')
def list_of_projects():
    projects = Project.query.all()
    return render_template('projects.html', projets=projects)


@app.route('/projects/<id>')
def show_detail_of_project(id):
    projects = Project.query.all()
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
    readable_date=readable_date, projects=projects)


@app.route('/contact')
def contact_me():
    projects = Project.query.all()
    return render_template('contact.html', projects=projects)


@app.route('/projects/new', methods=['GET', 'POST'])
def create_new_project():
    projects = Project.query.all()
    if request.form:
        split_date = request.form['date'].split('-')
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
    return render_template('add_project.html', projects=projects)


@app.route('/project/<id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    if request.form:
        split_date = request.form['date'].split('-')
        year = int(split_date[0])
        month = int(split_date[1])
        day = int(split_date[2])
        date_to_submit = datetime.date(year, month, day)
        project.title = request.form['title']
        project.completion_date = date_to_submit
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.github_link = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_project.html', project=project, projects=projects)


@app.route('/project/<id>/delete')
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    projects = Project.query.all()
    return render_template('404.html', msg=error, projects=projects), 404
    
    
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')