import asyncio
import time


async def tick():
    await asyncio.sleep(1)
    return 'Tick'


async def tock():
    await asyncio.sleep(2)
    return 'Tock'


async def main():
    start = time.perf_counter()

    t1 = asyncio.create_task((tick()))
    t2 = asyncio.create_task((tock()))

    # await for all functions to complete
    # results = await asyncio.gather(t1, t2)
    # for i, result in enumerate(results, start=1):
    #     elapsed = time.perf_counter() - start
    #     print(f'Executed {i} in {elapsed:0.2f} seconds')
    #     print(result)

    # prints as some is done
    for i, t in enumerate(asyncio.as_completed((t1, t2)), start=1):
        result = await t
        elapsed = time.perf_counter() - start
        print(f'Executed {i} in {elapsed:0.2f} seconds')
        print(result)


if __name__ == '__main__':
    asyncio.run(main())