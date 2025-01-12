import os
import magic
from secml.array import CArray

from secml_malware.models.malconv import MalConv
from secml_malware.models.c_classifier_end2end_malware import CClassifierEnd2EndMalware, End2EndModel
from secml_malware.attack.whitebox.c_header_evasion import CHeaderEvasion
from secml_malware.attack.whitebox import CKreukEvasion

net = MalConv()
net = CClassifierEnd2EndMalware(net)
net.load_pretrained_model()


partial_dos = CHeaderEvasion(net, random_init=False, iterations=50, optimize_all_dos=False, threshold=0.5)

folder = "../data/malware_samples/"
X = []
y = []
file_names = []
for i, f in enumerate(os.listdir(folder)):
    path = os.path.join(folder, f)
    print(path)
    #if 'petya' not in path:
    #    continue
    #if "PE32" not in magic.from_file(path):
    #    continue
    with open(path, "rb") as file_handle:
        code = file_handle.read()
    x = End2EndModel.bytes_to_numpy(
        code, net.get_input_max_length(), 256, False
    )
    _, confidence = net.predict(CArray(x), True)

    if confidence[0, 1].item() < 0.5:
        print("Not added with confidence : ", confidence[0, 1].item(), "\n")
        continue

    print(f"> Added {f} with confidence {confidence[0,1].item()}\n")
    X.append(x)
    conf = confidence[1][0].item()
    y.append([1 - conf, conf])
    file_names.append(path)

for sample, label in zip(X, y):
    y_pred, adv_score, adv_ds, f_obj = partial_dos.run(CArray(sample), CArray(label[1]))
    print(partial_dos.confidences_)
    print(f_obj)

# Reconstruct the sample from the adversarial
print("\n\nReconstruction \n")

adv_x = adv_ds.X[0,:]
real_adv_x = partial_dos.create_real_sample_from_adv(file_names[0], adv_x)
print(len(real_adv_x))
real_x = End2EndModel.bytes_to_numpy(real_adv_x, net.get_input_max_length(), 256, False)
_, confidence = net.predict(CArray(real_x), True)
print(confidence[0,1].item())
