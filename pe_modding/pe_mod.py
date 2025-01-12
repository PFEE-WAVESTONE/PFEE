import pefile

class PEMod:
    def __init__(self, path):
        self.path = path
        self.pe = pefile.PE(self.path)

    def sections_pretty_print(self):
        for section in self.pe.sections:
            print(section.Name.decode('utf-8'))
            print("\tVirtual Address: " + hex(section.VirtualAddress))
            print("\tVirtual Size: " + hex(section.Misc_VirtualSize))
            print("\tRaw Size: " + hex(section.SizeOfRawData))

    def sections_list(self):
        return [[section.Name.decode('utf-8'), section.VirtualAddress,
                 section.Misc_VirtualSize, section.SizeOfRawData] for section in self.pe.sections]

    def datas_pretty_print(self):
        for data_dir in self.pe.OPTIONAL_HEADER.DATA_DIRECTORY:
            print(data_dir)

    def datas_list(self):
        return [data_dir for data_dir in self.pe.OPTIONAL_HEADER.DATA_DIRECTORY]

    def sample_code_inject(self):
        pass

    def save(self, out_file_path):
        self.pe.write(out_file_path)

if __name__ == "__main__":
    notemod = PEMod("../data/malware_samples/YouAreAnIdiot.exe")
    notemod.sections_pretty_print()
    print(notemod.sections_list())
