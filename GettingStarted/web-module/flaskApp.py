from flask import Flask, render_template
from Student import Student

app = Flask(__name__)


@app.route('/')
def hello():
    student = Student()
    student.read_file()
    return render_template('template.html', my_string="Wheeeee!", my_list=student.students)


if __name__ == '__main__':
    app.run()
