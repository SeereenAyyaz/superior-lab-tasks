class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

    def display_info(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")


class UndergraduateCourse(Course):
    def __init__(self, course_code, course_name, year_level):
        super().__init__(course_code, course_name)
        self.year_level = year_level

    def additional_info(self):
        print(f"Year Level: {self.year_level}")


class GraduateCourse(Course):
    def __init__(self, course_code, course_name, research_area):
        super().__init__(course_code, course_name)
        self.research_area = research_area

    def additional_info(self):
        print(f"Research Area: {self.research_area}")


def register_course():
    course_type = input("Enter course type (undergraduate/graduate): ").strip().lower()
    course_code = input("Enter the course code: ").strip()
    course_name = input("Enter the course name: ").strip()

    if course_type == 'undergraduate':
        year_level = input("Enter the year level: ").strip()
        course = UndergraduateCourse(course_code, course_name, year_level)
    elif course_type == 'graduate':
        research_area = input("Enter the research area: ").strip()
        course = GraduateCourse(course_code, course_name, research_area)
    else:
        print("Invalid course type. Please enter either 'undergraduate' or 'graduate'.")
        return None

    print("\nCourse Registration Successful!")
    course.display_info()
    course.additional_info()


register_course()

