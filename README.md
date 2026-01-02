# add objects to the db manually
>>>from app import app, db, Project
>>> from models import Project
>>> app.app_context().push()
>>> p = Project(username="luis", email="some@test.com")
>>> db.session.add(p)
>>> db.session.commit()


# new and edit routes use the same form template

jinja block button
- Correct approach
Navigation belongs outside block content.
<section class='navigaction>