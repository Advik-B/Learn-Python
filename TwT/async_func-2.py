import asyncio


async def fetch_data():
    print('Start fetching')
    await asyncio.sleep(2)
    print('Fetching done')
    return {'data': 1}

async def print_num():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_num())
    val = await task1
    print(val)
    await task2

asyncio.run(main())
