import redis, time, aioredis, asyncio
"""
r = redis.Redis(host='localhost', port=6379, db=0)
p = r.pubsub()

p.subscribe('my-first-channel')
r.publish('my-first-channel', 'some data')
r.publish('my-first-channel', 'some data')

print(p.get_message())
print(p.get_message())
print(p.get_message())


r.hset("sessions", "12345", 20)
r.expire("sessions", 10)

time.sleep(9)

print(r.hget("sessions", "12345"))

#for message in p.listen():
#    print(message)

p.close()

"""


async def first():
    for i in range(100):
        print("first ", i)


async def second():
    for i in range(100):
        print("second ", i)


async def main():
    d1 = loop.create_task(first())
    d2 = loop.create_task(second())
    await asyncio.wait([d1, d2])



loop = asyncio.get_event_loop()
app = loop.run_until_complete(main())


