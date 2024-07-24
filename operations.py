from database import DataBase
from models import User

class Operation:

    def __init__(self) -> None:
        self.db = DataBase()

    async def insert_data(self):
        async with self.db.get_session() as session:
            user = User()
            user.id = 1
            user.name = "rashed"
            user.age = 25
            user.proffession = "SWE"

            session.add(user)
            await session.commit()