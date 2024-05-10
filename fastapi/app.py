from fastapi import FastAPI, Depends, Form, Request
from sqlalchemy.orm import Session
from models import Book, SessionLocal, create_db_and_tables
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


# Initialize database
@app.on_event("startup")
def startup_event():
    create_db_and_tables()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_books(request: Request, db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return templates.TemplateResponse(
        "index.html", {"request": request, "books": books}
    )


@app.post("/book/")
async def create_book(
    request: Request,
    title: str = Form(...),
    author: str = Form(...),
    rating: float = Form(...),
    db: Session = Depends(get_db),
):
    book = Book(title=title, author=author, rating=rating)
    db.add(book)
    db.commit()
    return templates.TemplateResponse(
        "index.html", {"request": request, "books": db.query(Book).all()}
    )
