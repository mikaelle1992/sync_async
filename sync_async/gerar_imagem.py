import uuid
from PIL import Image


def header():
    print('getting file')
    print("converting file")


def generator_random():
    valor = uuid.uuid4().hex
    return valor.replace("-", "")


def convert_image(path, name_file):
    image1 = Image.open(path)
    pdf = image1.convert('RGB')
    pdf.save(name_file+".pdf")
    return pdf


def main():
    header()
    generator_ = generator_random()
    convert_image("teste_imagem.jpg", generator_)
    print("finished")

if __name__ == '__main__':
    main()