# [START imports]
from google.appengine.ext import ndb
#[END imports]

DEFAULT_PROJECT_NAME = 'default_project_db'

def project_db_key(project_db_name=DEFAULT_PROJECT_NAME):
    return ndb.Key('Project', project_db_name)

# [START User]
class User(ndb.Model):
    identity = ndb.StringProperty(indexed=True,required=True)
    email = ndb.StringProperty(indexed=True,required=True)
    type = ndb.StringProperty()
    isFirstLogin = ndb.BooleanProperty(default=True)
    password = ndb.StringProperty()
    projectIds = ndb.StringProperty(repeated=True)

# [START Project]
class Project(ndb.Model):
    projectId = ndb.StringProperty(indexed=True, required=True)
    due_date = ndb.DateTimeProperty(required=True)
    userIds = ndb.StringProperty(repeated=True)
    requirements = ndb.StringProperty(repeated=True)
    defaultPassword = ndb.StringProperty()
    department = ndb.StringProperty()
    group = ndb.StringProperty()
    description = ndb.StringProperty()

# [START Entry]
class Entry(ndb.Model):
    project = ndb.StructuredProperty(Project, indexed=True, required=True)
    user = ndb.StructuredProperty(User, indexed=True, required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)
    weights = ndb.StringProperty(repeated=True)
    requirements = ndb.StringProperty(repeated=True)
    requirements_output = ndb.StringProperty(repeated=True)
