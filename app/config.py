import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

COMPLETED_COURSES_FILE = os.path.join(BASE_DIR, "database", "courses", "completed_courses.json")

ONGOING_COURSES_FILE = os.path.join(BASE_DIR, "database", "courses", "ongoing_courses.json")

LIVE_SESSIONS_FILE = os.path.join(BASE_DIR, "database", "dashboard", "live_sessions.json")

MY_COURSES_FILE = os.path.join(BASE_DIR, "database", "dashboard", "my_courses.json")

OVERVIEW_FILE = os.path.join(BASE_DIR, "database", "dashboard", "over_all_informations.json")

PRODUCTIVITY_FILE = os.path.join(BASE_DIR, "database", "dashboard", "productivity.json")

TOP_COURSES_FILE = os.path.join(BASE_DIR, "database", "dashboard", "top_courses.json")

COURSE_CONTENTS_FILE = os.path.join(BASE_DIR, "database", "explore-course", "course_contents.json")

QUES_ANS_FILE = os.path.join(BASE_DIR, "database", "explore-course", "ques_answer.json")

MESSAGE_FILE = os.path.join(BASE_DIR, "database", "message", "message.json")

PAYMENT_FILE = os.path.join(BASE_DIR, "database", "payment", "payment.json")

TEACHERS_FILE = os.path.join(BASE_DIR, "database", "teacher", "teachers.json")

LIVE_HISTORY_FILE = os.path.join(BASE_DIR, "database", "live-session", "live_history.json")

LIVE_ONGOING_FILE = os.path.join(BASE_DIR, "database", "live-session", "live_ongoing.json")

LIVE_PARTICIPANTS_FILE = os.path.join(BASE_DIR, "database", "live-session", "live_participants.json")