#!/usr/bin/env python3
'''Module 1
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''delay of certain number of s
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
