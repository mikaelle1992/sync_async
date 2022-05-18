import asyncio


async def calculadora():
    print("Calculadora\n Subtração")
    await asyncio.sleep(4)
    print("Soma")
    await asyncio.sleep(5)
    print("fim")


async def soma(valor):
    for i in range(10):
        resposta = valor + i
        print(f'{valor} + {i}=', resposta)
        await asyncio.sleep(0.25)


async def subtracao(valor):
    for i in range(10):
        resposta = valor - i
        print(f'{valor} - {i}=', resposta)
        await asyncio.sleep(0.25)


async def main():
    task1 = asyncio.create_task(calculadora())
    task3 = asyncio.create_task(subtracao(50))
    await asyncio.sleep(5)
    task2 = asyncio.create_task(soma(2))

    value = await task1
    print(value)
    await task2
    await task3

asyncio.run(main())