import os

import magic
import numpy as np
from secml.array import CArray

from secml_malware.attack.blackbox.c_wrapper_phi import CEnd2EndWrapperPhi
from secml_malware.attack.blackbox.ga.c_base_genetic_engine import CGeneticAlgorithm
from secml_malware.attack.blackbox.c_gamma_sections_evasion import CGammaSectionsEvasionProblem
from secml_malware.models.c_classifier_end2end_malware import CClassifierEnd2EndMalware
from secml_malware.models.malconv import MalConv

net = CClassifierEnd2EndMalware(MalConv())
net.load_pretrained_model()
net = CEnd2EndWrapperPhi(net)

# Extraction of the goodware and creation of the attack
goodware_folder = '../data/goodware_samples' 
section_population, what_from_who = CGammaSectionsEvasionProblem.create_section_population_from_folder(goodware_folder, how_many=10, sections_to_extract=['.rdata'])

attack = CGammaSectionsEvasionProblem(section_population, net, population_size=10, penalty_regularizer=1e-6, iterations=10, threshold=0)

# Net prediction, add the predicted malware in X
folder = '../data/malware_samples/'
X = []
y = []
file_names = []
for i, f in enumerate(os.listdir(folder)):
    path = os.path.join(folder, f)
    if "PE32" not in magic.from_file(path):
        continue
    with open(path, "rb") as file_handle:
        code = file_handle.read()
    x = CArray(np.frombuffer(code, dtype=np.uint8)).atleast_2d()
    _, confidence = net.predict(x, True)

    if confidence[0, 1].item() < 0.5:
        continue

    print(f"> Added {f} with confidence {confidence[0,1].item()}")
    X.append(x)
    conf = confidence[1][0].item()
    y.append([1 - conf, conf])
    file_names.append(path)

# Attack
engine = CGeneticAlgorithm(attack)
for sample, label in zip(X, y):
    print(sample, label[1])
    if label[1] == 1:
        continue
    y_pred, adv_score, adv_ds, f_obj = engine.run(sample, CArray(label[1]))
    print(engine.confidences_)
    print(f_obj)