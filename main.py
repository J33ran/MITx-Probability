import comp_prob_inference
import matplotlib.pyplot as plt

import sys
from simpsons_paradox_data import *

prob_table = {('sunny', 'hot'): 3/10,
('sunny', 'cold'): 1/5,
('rainy', 'hot'): 1/30,
('rainy', 'cold'): 2/15,
('snowy', 'hot'): 0,
('snowy', 'cold'): 1/3
}


adm_dept = joint_prob_table[gender_mapping['male'], department_mapping['F']]
print (adm_dept/np.sum(adm_dept))

# female_only = dict(zip(department_mapping, joint_prob_table[gender_mapping['female']]))
# print(female_only)

# joint_prob_gender_admission = joint_prob_table.sum(axis=1)
# print(joint_prob_gender_admission)


# admitted_only = joint_prob_gender_admission[:, admission_mapping['admitted']]
# print(admitted_only)

sys.exit(0)