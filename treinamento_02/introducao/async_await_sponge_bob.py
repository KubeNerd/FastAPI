# chapar pão
# fritar hamburger
# montar sanduiche
# fazer milk shake

# from time import sleep

# class SyncSpongeBob:
#     def cook_bread(self):
#         sleep(3)

#     def cook_hamburger(self):
#         sleep(10)
    
#     def mount_sandwich(self):
#         sleep(3)
    
#     def make_milkshare(self):
#         sleep(5)


#     def cook(self):
#         self.cook_bread()
#         self.cook_hamburger()
#         self.mount_sandwich()
#         self.make_milkshare()


# sync_spongebob = SyncSpongeBob()
# sync_spongebob.cook()


# # Async/AWAIT

# class SyncSpongeBob:
#     async def cook_bread(self):
#         sleep(3)

#     async def cook_hamburger(self):
#         sleep(10)
    
#     async def mount_sandwich(self):
#         sleep(3)
    
#     async def make_milkshare(self):
#         sleep(5)


#     async def cook(self):
#         self.cook_bread()
#         self.cook_hamburger()
#         self.mount_sandwich()
#         self.make_milkshare()


# sync_spongebob = SyncSpongeBob()
# sync_spongebob.cook()


import asyncio

class AsyncSpongeBob:
    async def cook_bread(self):
        print("Chapeando o pão...")
        await asyncio.sleep(3)
        print("Pão pronto.")

    async def cook_hamburger(self):
        print("Fritando o hambúrguer...")
        await asyncio.sleep(10)
        print("Hambúrguer pronto.")

    async def mount_sandwich(self):
        print("Montando o sanduíche...")
        await asyncio.sleep(3)
        print("Sanduíche pronto.")

    async def make_milkshake(self):
        print("Fazendo milkshake...")
        await asyncio.sleep(5)
        print("Milkshake pronto.")

    async def cook(self):
        await self.cook_bread()
        await self.cook_hamburger()
        await self.mount_sandwich()
        await self.make_milkshake()

# Execução do processo assíncrono
if __name__ == "__main__":
    spongebob = AsyncSpongeBob()
    asyncio.run(spongebob.cook())
