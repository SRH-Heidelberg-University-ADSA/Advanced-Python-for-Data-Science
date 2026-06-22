import asyncio
import time


async def worker(seconds, future):
    await asyncio.sleep(seconds)
    print("worker completed")
    #return seconds
    future.set_result(seconds)

def future_has_arrived(future):
    print(f'future has arrived with {future.result()}')

async def begin_work():
    print(f'program started at {time.strftime('%X')}')

    #await worker(2)
    #await worker(3)
    #task1 = asyncio.create_task(worker(2))
    #task2 = asyncio.create_task(worker(3))
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    future1.add_done_callback(future_has_arrived)
    future2.add_done_callback(future_has_arrived)

    await asyncio.gather(*[ worker(x,future) for x,future in [(2,future1),(3,future2)]] )
    #await task1
    #await task2
    #print(result)
     
    print(f'finished at {time.strftime('%X')}')

asyncio.run(begin_work())
