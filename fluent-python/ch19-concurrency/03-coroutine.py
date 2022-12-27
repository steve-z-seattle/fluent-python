import asyncio
import itertools

def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')
    
async def supervisor() -> int:
    spinner = asyncio.create_task(spin('thining!'))
    print(f'spinner object: {spinner}')
    result = await slow()
    spinner.cancel()
    return result

async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
        # if done.wait(.1):
        #     break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')   

async def slow() -> int:
    await asyncio.sleep(3)
    return 42

if __name__ == '__main__':
    main()
