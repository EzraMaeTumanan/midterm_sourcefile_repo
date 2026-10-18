# PART A
# Parent class for basic student information.
class Student:
    def __init__(self, name, course, year_level):
        # Store the three values in instance attributes.
        self.name = name
        self.course = course
        self.year_level = year_level

    def get_profile(self):
        # Return the student's information using HTML-like tags.
        return (
            f"<h2>{self.name}</h2>\n"
            f"<p>Course: {self.course}</p>\n"
            f"<p>Year Level: {self.year_level}</p>"
        )

# PART B
# Child class for an IT student (inherits from Student).
class ITStudent(Student):
    # Class attribute: the student's programming skill.
    skill = "Python"

    def get_skill(self):
        # Return the programming skill using a <p> tag.
        return f"<p>Programming Skill: {self.skill}</p>"

# PART C
# Application class with Flask-inspired routes.
class StudentApp:
    def __init__(self, title, student):
        # Store the title and the student object.
        self.title = title
        self.student = student

    def route(self, path):
        # Return the correct content based on the route path.
        if path == "/":
            return f"<h1>{self.title}</h1>"
        elif path == "/profile":
            # Uses both the inherited method and the child's own method.
            return self.student.get_profile() + "\n" + self.student.get_skill()
        else:
            return "<h1>404 - Page Not Found</h1>"

    def run(self):
        # Print the app title, then test the required routes.
        print(f"Running: {self.title}\n")
        for path in ["/", "/profile", "/unknown"]:
            print(f"GET {path}")
            print(self.route(path))
            print()

# PART D
# Create the student and application objects.
student = ITStudent("Ezra Mae R. Tumanan", "BS Information Technology", 4)
app = StudentApp("PSU Student Profile App", student)

# Start the application.
app.run()