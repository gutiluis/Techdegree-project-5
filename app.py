from flask import render_template, url_for, request, redirect, Flask
from models import db, Project, app


# url_for connects html to views

@app.route('/')
def index():
    project = Project.query.all()
    return render_template('index.html', project=project)


@app.route('/projects/new', methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        project = Project(
            title=request.form['title'],
            description=request.form['description'],
            skills=request.form['skills'],
            github_repo=request.form['githubrepo'])
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


# test
@app.route('/project_detail/<id>')
def project_detail(id):
    project = Project.query.get_or_404(id)
    if request.form:
        project.title = request.form['title']
        project.description = request.form['description']
        project.skills = request.form['skills']
        project.github_repo = request.form['githubrepo']
    return render_template('detail.html', project=project)



# test
@app.route('/projects/<id>/edit', methods=["GET", "POST"])
def project_edit(id):
    project = Project.query.get_or_404(id)
    if request.form:
        project.title = request.form["title"] # created is discontinued
        project.description = request.form['description']
        project.skills = request.form['skills']
        project.github_repo = request.form['githubrepo']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', project=project) # the edit.html is the same as projectform.html. new is empty and edit with existing data


# test
@app.route('/projects/<id>/delete')
def project_delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/about')
def project_about():
    return render_template('about.html')

# test
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=9000, host='127.0.0.1')
