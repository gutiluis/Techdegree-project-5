from flask import render_template, url_for, request, redirect
from datetime import datetime
from models import db, Project, app


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/projects/new', methods=["GET", "POST"])
def add_project():
    if request.method == "POST":

        year_and_month = request.form.get('date')
        # model takes datetimeobject in column
        convert_string = datetime.strptime(year_and_month, "%Y-%m").date()

        new_project = Project(
            # get is a method needs parentheses
            title=request.form.get('title'),
            created=convert_string,
            description=request.form.get('desc'),
            skills=request.form.get('skills'),
            github_repo=request.form.get('github'))

        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


@app.route('/projects/<id>')
def project_detail(id):
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project)


@app.route('/projects/<id>/edit', methods=["GET", "POST"])
def project_edit(id):
    """ same conventions from add project"""
    project = Project.query.get_or_404(id)
    if request.method == 'POST':

        year_and_month = request.form.get('date')
        convert_string = datetime.strptime(year_and_month, "%Y-%m").date()

        project.title = request.form.get('title')
        project.created = convert_string
        project.description = request.form.get('desc')
        project.skills = request.form.get('skills')
        project.github_repo = request.form.get('github')
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editform.html', project=project)


@app.route('/projects/<id>/delete')
def project_delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/about')
def about_me():
    return render_template('about.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == "__main__":
    with app.app_context():  # proxy
        db.create_all()
    app.run(debug=True, port=9000, host='127.0.0.1')
