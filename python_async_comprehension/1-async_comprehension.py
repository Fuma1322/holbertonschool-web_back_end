#!/usr/bin/env python3
"""
Contains the async_comprehension coroutine
"""

import asyncio
from typing import List
from random import uniform

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over async_generator.
    """
    return [i async for i in async_generator()]


async def main():
    """
    Main coroutine to demonstrate the usage of async_comprehension.
    """
    print(await async_comprehension())

if __name__ == "__main__":
    asyncio.run(main())
