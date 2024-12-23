import aioredis


async def get_redis_connection():
    return await aioredis.create_redis_pool('redis://localhost')
