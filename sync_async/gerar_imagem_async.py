import base64
import asyncio
import uuid
from PIL import Image


async def convert_image(path, name_file):
    image1 = Image.open(path)
    pdf = image1.convert('RGB')
    pdf.save(name_file+".pdf")
    await asyncio.sleep(1)
    return pdf
    

async def generator_random():
    valor = uuid.uuid4().hex
    await asyncio.sleep(1)
    return valor.replace("-", "")

async def header():
    print('getting file')
    await asyncio.sleep(0.5)
    print("converting file")
    await asyncio.sleep(0.5)

async def main():

    task = asyncio.create_task(header())
    task1 = asyncio.create_task(generator_random())
    generator_ = str(await task1)
    task2 = asyncio.create_task(convert_image("teste_imagem.jpg", generator_))
    await task2
    
    await task
    print("finished")

asyncio.run(main())
