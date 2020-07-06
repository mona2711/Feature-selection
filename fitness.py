import aiohttp
import requests
import asyncio
import generation
import json
from generation import next_generation
import individual

async def request(session,url,individual):
    data={'features':str(individual.features)}
    async with session.post(url=url,data=data) as response:
        response = await response.read()
        print(response.decode('utf-8'))
        individual.fitness=float(response.decode('utf-8'))
        return response

async def schedule_workers(urls,generation,start):
    tasks=[]
    i=start
    async with aiohttp.ClientSession() as session:
        for url in urls:
            print(i)
            tasks.append(request(session, url,generation[i]))
            i=i+1
            if(i>=len(generation)):
                break
        await asyncio.gather(*tasks)

async def run(generation):
    urls = [
            'http://18.218.193.96:80/search'
        ]
    i=0
    while(i<len(generation)):
        await schedule_workers(urls,generation,i)
        i=i+len(urls)
    
    for individual in generation:
        print(individual.fitness)

def compute_fitness(generation):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(generation))