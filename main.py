from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from routers.courses import completed_course, ongoing_course
from routers.dashboard import (
    live_sessions,
    my_courses,
    over_all_informations,
    productivity,
    top_courses,
)
from routers.explorecourse import course_contents, ques_answer
from routers.message import message
from routers.payment import payment
from routers.teachers import teachers
from routers.livesession import live_history, live_ongoing, live_participants

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# Serve assets folder at /assets
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# Include routers
app.include_router(completed_course.router)
app.include_router(ongoing_course.router)
app.include_router(live_sessions.router)
app.include_router(my_courses.router)
app.include_router(over_all_informations.router)
app.include_router(productivity.router)
app.include_router(top_courses.router)
app.include_router(course_contents.router)
app.include_router(ques_answer.router)
app.include_router(message.router)
app.include_router(payment.router)
app.include_router(teachers.router)
app.include_router(live_history.router)
app.include_router(live_ongoing.router)
app.include_router(live_participants.router)
