from typing import Optional
from fastapi import Body,FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# class for fixing a data structure
class Book:
    id:int
    title:str
    author: str
    description: str
    rating: int

    def __init__ (self, id, title,author, description, rating):
        self.id=id
        self.title=title
        self.author = author
        self.description =description
        self.rating=rating


# data validation for the data coming in the body.
class BookRequest(BaseModel):
    id: Optional[int] =Field(title='id is not needed')
    title:str =Field(min_length=3)
    author:str =Field(min_length=1)
    description:str=Field(min_length=1, max_length=100)
    rating:int =Field(gt=-1, lt=6)

    #Example pydantic config data for the swagger UI. 
    class Config:
        json_schema_extra = {
            'example':{
                'title':'a new book',
                'author': 'author name',
                'description': 'book description',                
                'rating': 'book rating'
            }
        }

# dummy database
BOOKS = [
    Book(1,'book title','author 404',' ehowihfweoiwf',5) 
]

# normal get api
@app.get("/books")
async def read_all_books():
    return BOOKS

# post api with pydantic validations
@app.post("/books/create")
async def create_book(body:BookRequest):
    # spreading the dict to book class 
    new_book = Book(**body.model_dump())

    # gives the json data
    # test_book = body.model_dump_json()
    # print(test_book)

    BOOKS.append(find_book_id(new_book))
    return new_book


# local function for setting the id.
def find_book_id(book:Book):
    if(len(BOOKS)> 0):
        book.id =BOOKS[-1].id + 1
    else:
        book.id = 1
    return book