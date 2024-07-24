import asyncio
from operations import Operation

async def main():
    op = Operation()
    await op.db.create_tables()
    await op.insert_data()

asyncio.run(main())