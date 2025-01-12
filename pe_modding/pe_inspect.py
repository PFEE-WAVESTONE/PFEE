import lief

exe_path = "./data/malware_samples/YouAreAnIdiot.exe"
exe_object = lief.parse(exe_path)

print('DOS Header')
print(exe_object.dos_header)

print('PE Header')
print(exe_object.header)

print('Optional Header')
print(exe_object.optional_header)

print('Sections')
for s in exe_object.sections:
	print(s.name, s.characteristics_lists)