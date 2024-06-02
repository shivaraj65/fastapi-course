from fastapi import Body,FastAPI

app = FastAPI()

class Book:
    id:int
    title:str
    author: str
    description: str
    rating: str

    def __init__ (self, id, title,author, description, rating):
        self.id=id
        self.title=title
        self.author = author
        self.description =description
        self.rating=rating

BOOKS = [
    Book(1,'book title','author 404',' ehowihfweoiwf','5') 
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("books/create")
async def create_book(body=Body()):
    BOOKS.append(body)
    return body