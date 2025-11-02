"""Downloding all json files from urls with async and sync"""
import time
import asyncio
import aiohttp
import aiofiles
import requests


urls = {
    'crime': 'https://data.lacity.org/api/views/2nrs-mtv8/rows.json?accessType=DOWNLOAD',
    'lottery': 'https://data.ny.gov/api/views/d6yy-54nr/rows.json?accessType=DOWNLOAD',
    'warehouse': 'https://data.montgomerycountymd.gov/api/views/v76h-r7br/rows.json?accessType=DOWNLOAD',
    'nutrition': 'https://data.cdc.gov/api/views/hn4x-zwk7/rows.json?accessType=DOWNLOAD',
    'drug_death_rate': 'https://data.cdc.gov/api/views/95ax-ymtc/rows.json?accessType=DOWNLOAD',
    'estate_sale': 'https://data.ct.gov/api/views/5mzw-sjtu/rows.json?accessType=DOWNLOAD'
}


# Async method 34.40s
SEM = asyncio.Semaphore(3) # max 3 files (1 finished -> 4 starts)


async def download_file(key, url, session):
    async with SEM:
        async with session.get(url) as response:
            async with aiofiles.open(f'{key}.json', 'wb') as file:
                # read data by 1 MB
                async for chunk in response.content.iter_chunked(1024 * 1024):
                    await file.write(chunk)
            print(f'✅ {key}.json uploaded.')
        

async def main():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        tasks = [download_file(key, url, session) for key, url in urls.items()]
        await asyncio.gather(*tasks)
    
        
# Sync method 92.21s
def download_file_sync(key, url):
    with requests.get(url) as response:
        with open(f'{key}.json', 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                file.write(chunk)
                print(f'Wrote {len(chunk)} bytes')
        print(f'{key}.json uploaded.')


def main_sync():
    for key, url in urls.items():
        download_file_sync(key, url)


if __name__ == '__main__':
    start = time.perf_counter()
    # main_sync()
    asyncio.run(main())
    result = time.perf_counter() - start
    print(f'It took {result:.2f}s.')