# async ko hm tb use krty hien jb at a time 1 sy zda task krny ho
# Normally 1 time pe 1 hi task hota he lkn async programming sy 1 time pe 1 sy zda task kr skty hein
# API 1 → wait 2 sec
# API 2 → wait 2 sec
# API 3 → wait 2 sec

# Normal code waits for each one:

# API 1 → API 2 → API 3
# 6 seconds

# Async code can start them together:

# API 1 ──┐
# API 2 ──┼──→ 2 seconds
# API 3 ──┘

import asyncio # asyncio ka use krty hein jb hm async programming krty hein iska purpose ye he k ye async programming ko handle krta he orr async programming me hm jb b kisi function ko call krty hein to usy await krna prta he

# Syntax:
# async def function_name():  kisi b function ko define krty time us k sth async likh lena he

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # await ka mtlb he k ye function wait kry ga jb tk ye task complete na ho jaye
    print("Data fetched!")
    
# async function ko run krny k lye hm asyncio.run() ka use krty hein    

asyncio.run(fetch_data())  # yaha pr run(main()) ka mtlb he k ye main function ko run krta he orr main function me fetch_data() ko await krta he

# agr hmary program me 1 sy zeda async function hein to hmy bar bar sb k sth run nai likhna prrta he hm sb async function ko main function me daal k run(main()) kr skty hein
async def main(): # main ko hm is lye use krty hein k ye async function ko run krta he 
    await fetch_data()
asyncio.run(main())  # yaha pr run(main()) ka mtlb he k ye main function ko run krta he orr jitny b function main function me hongy wo sb at a time run ho jaye gy 


# For multiple async functions, you can define them and call them within the main function. Here's an example:
async def fetch_users():
    print("Fetching users...")
    await asyncio.sleep(2)
    print("Users fetched!")
async def fetch_orders():
    print("Fetching orders...")
    await asyncio.sleep(2)
    print("Orders fetched!")
async def fetch_products():
    print("Fetching products...")
    await asyncio.sleep(2)
    print("Products fetched!")

async def main():
    await asyncio.gather(
        fetch_users(),
        fetch_orders(),
        fetch_products()
    )
asyncio.run(main())  # yaha pr run(main()) ka mtlb he k ye main function ko run krta he orr jitny b function main function me hongy wo sb at a time run ho jaye gy