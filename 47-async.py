import time
import asyncio

async def endpoint(route: str) -> str:
    print(f">> handling {route}")
    
    # emulate database delay
    await asyncio.sleep(1)
    
    print(f"<< response {route}")
    return route




async def server():
    # Run test requests
    tests = (
        "GET /shipment?id=1",
        "PATCH /shipment?id=4",
        "GET /shipment?id=3",
    )

    start = time.perf_counter()
    
    for route in tests:
        # asyncio.run (x)
        result=  await endpoint(route)
        print("Result back: ", result)

    end = time.perf_counter()
    print(f"Time taken: {end - start:.2f}s")


# Run server
asyncio.run(server())
