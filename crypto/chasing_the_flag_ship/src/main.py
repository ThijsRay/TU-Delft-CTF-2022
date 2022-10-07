import asyncio
import random
from os import environ
from struct import unpack
from textwrap import wrap
from collections import deque
from quart import Quart, request, Response
from hypercorn.config import Config
from hypercorn.asyncio import serve
from ipaddress import ip_address

app = Quart(__name__)

ocean = "2a02:c206:2101:8992"

MAX_ISLANDS = 1000
SAILING_SPEED = 10
previous_sightings = deque(maxlen=MAX_ISLANDS)

def bits_to_hex(bits):
    return ':'.join(wrap(hex(bits)[2:].rjust(16, '0'), 4))


def get_island():
    return str(ip_address(f"{ocean}:{bits_to_hex(random.getrandbits(64))}"))


def add_sighting():
    sighting = get_island()
    previous_sightings.appendleft(sighting)


def store_older_sightings():
    random.seed()
    for _ in range(MAX_ISLANDS):
        add_sighting()
    print(previous_sightings)


async def search_for_previous_sights(in_area):
    try:
        current = previous_sightings.index(in_area)
        if current+1 < len(previous_sightings):
            return (previous_sightings[current], previous_sightings[current+1])
        else:
            return (previous_sightings[current], None)
    except:
        return (None, None)

def most_recent_sighting():
    return f"{previous_sightings[1]}"

async def receive_new_sightings():
    while True:
        add_sighting()
        print(f"Flag ship sailed to http://[{previous_sightings[0]}]")
        await asyncio.sleep(SAILING_SPEED)


async def parse_island(area):
    if len(area) > 8:
        try:
            return str(ip_address(area[1:-1]))
        except Exception as e:
            return None
    else:
        return None

def never_seen():
    mrs = most_recent_sighting()
    return Response(f"""
Hmmm... The flag ship does not seem to have visited
this place recently. Rumor has it that it stayed at
<a href='http://[{mrs}]'>{mrs} island</a> until very recently\n
           """)

@app.route("/")
async def area():
    host = request.headers['Host']
    island = await parse_island(host)
    if island is None:
        return never_seen()
    else:
        if island == previous_sightings[0]:
            return Response(f"""
Just in time! You see the flag ship in the distance! You take your binoculars
and try catch a glimpse from afar. The name of the flag ship is
barely visible, but you manage to read it before it sails to
yet another island. The ship carries the name {environ['FLAG']}
            """)
        elif island == previous_sightings[1]:
            return Response(f"""
There are clear signs that the flag ship was here just a few
moments ago. Nobody knows where it went, but the local harbormaster
seems to have some information about the flag ship's previous
destination. You are told that the ship was previously spotted in
the harbor of <a href='http://[{previous_sightings[2]}]'>
{previous_sightings[2]} island</a>. Maybe ask around over there?"
            """)

        current, previous = await search_for_previous_sights(island)
        if current is None:
            return never_seen()
        if previous is None:
            return Response(f"""
There seems to be no beginning to this ships journey. You enter
the office of the harbormaster once again and request the records
of the flag ship. Unfortunately, they have just been removed (as is
required after {MAX_ISLANDS * SAILING_SPEED} seconds).

"Too bad! It all happens automatically", the harbormaster says. "But
if manage to you catch up to this ship, tell Captain M. Twister that
their port dues are still unpaid!"
""")
        else:
            return Response(f"""
It has been a while since the flag ship showed up on {current} island.
Luckily for you, islands in this area are required by law to keep public
records of all vessels that have entered their harbors and where they came
from. According to those records, the flag ship came from
<a href='http://[{previous}]'>{previous} island</a>.
            """)


async def main():
    config = Config()
    config.bind = ["localhost:8080"]

    await asyncio.gather(
        serve(app, config),
        receive_new_sightings()
    )


if __name__ == "__main__":
    store_older_sightings()

    asyncio.run(main())
