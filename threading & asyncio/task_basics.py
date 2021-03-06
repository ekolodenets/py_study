import asyncio

async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')


async def main():
    t1 = asyncio.create_task(tick(), name='tick1')
    t2 = asyncio.ensure_future(tick())

    # await t1
    # await t2
    
    # or
    await asyncio.gather(t1, t2)

    print(f'{t1.get_name()}. Done = {t1.done()}')
    print(f'{t2.get_name()}. Done = {t2.done()}')

if __name__ == '__main__':
    asyncio.run(main())