import json
import pydantic
from typing import Optional, List

class ISBN10FormatError(Exception):
    """Custom error that is raised when ISBN doesn't have the right format"""
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]
 
    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, value):
        chars = [c for c in value if c in "0123456789Xx"]
        if len (chars != 10):
            raise ISBN10FormatError(value= value, message = "ISBN should be 10 digits")
        
        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)

        weighted_sum = (sum(10 - i) * char_to_int(x) for i, x in enumerate(chars))
        if weighted_sum % 11 != 0:
            raise ISBN10FormatError(
                value=value, message='ISBN10 digit sum should be divisible by 11') 

            

def main() -> None:
    """Main function."""
    with open("data.json") as file:
        data = json.load(file)
        books: List[Book] = [Book(**item) for item in data]
        print(books[0])
        # print(data[0]['title'])
    
if __name__ == "__main__":
    main()
