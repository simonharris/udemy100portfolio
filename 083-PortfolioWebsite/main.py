from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


## config ---------------------------------------------------------------------


app = Flask(__name__)

# Connect to Database
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


## library --------------------------------------------------------------------


class Project(db.Model):

    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    headline: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(1024), unique=True, nullable=False)
    thumbnail: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# def get_random_cafe():
#     with app.app_context():
#         return db.session.execute(db.select(Cafe).order_by(func.random()).limit(1)).scalar()


def get_all_projects():
    with app.app_context():
        return db.session.execute(db.select(Project).order_by(Project.name)).scalars().all()




## routes ---------------------------------------------------------------------


@app.route('/')
def home():
    return render_template('index.html') #, all_posts=posts)


@app.route('/api/list')
def api_list():
    projects = get_all_projects()
    return jsonify(projects=[project.to_dict() for project in projects])


## main -----------------------------------------------------------------------


if __name__ == "__main__":
    app.run(debug=True, port=5000)

