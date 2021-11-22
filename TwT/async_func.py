import asyncio

async def main():
    print('Start of main')
    tsk = asyncio.create_task(foo('Heloo'))
    await asyncio.sleep(0.5)
    print('End of main')

async def foo(text: str):
    print(text)
    await asyncio.sleep(10)

asyncio.run(main())