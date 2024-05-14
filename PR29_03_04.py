class Computer:
    def __init__(self, processor, ram, gpu):
        self.__processor = processor
        self.__ram = ram
        self.__gpu = gpu

    def get_processor(self):
        return self.__processor

    def get_ram(self):
        return self.__ram

    def get_gpu(self):
        return self.__gpu

    def set_processor(self, processor):
        self.__processor = processor

    def set_ram(self, ram):
        self.__ram = ram

    def set_gpu(self, gpu):
        self.__gpu = gpu

computer = Computer("Intel Core i5", "8GB", "NVIDIA GeForce GTX 1650")

print("Процесор:", computer.get_processor())
print("ОЗУ:", computer.get_ram())
print("Відеокарта:", computer.get_gpu())

computer.set_ram("16GB")
print("Нова конфігурація ОЗУ:", computer.get_ram())