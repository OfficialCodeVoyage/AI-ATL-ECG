result = """*1dAVb:** 1st degree AV block

**RBBB:** right bundle branch block

**LBBB:** left bundle branch block

**SB:** sinus bradycardia

**AF:** atrial fibrillation

**ST:** sinus tachycardia

**Patient:** 60 years old, male

**Percentage likelihoods:**

1dAVb: 0.17332049

RBBB: 0.0024566373

LBBB: 8.599876e-05

SB: 4.6350953e-05

AF: 0.0020524128

ST: 7.276859e-05


The patient is 60 years old and male, and has a 17.3% likelihood of having 1st degree AV block. This is a relatively common condition, and is usually not a cause for concern. However, it is important to monitor the patient's heart rate and rhythm, and to rule out other causes of heart block.

The patient also has a 0.02% likelihood of having right bundle branch block, a 0.0001% likelihood of having left bundle branch block, a 0.0005% likelihood of having sinus bradycardia, a 0.002% likelihood of having atrial fibrillation, and a 0.0001% likelihood of having sinus tachycardia. These are all very rare conditions, and are unlikely to be causing any symptoms.

Overall, the patient's ECG results are normal. However, it is important to monitor the patient's heart rate and rhythm, and to rule out other causes of heart block.
"""

def take_recommendation(result):
    split = result.split("**Recommendations:**",1)
    print(len(split))
    print("**Recommendations:**" + split[1])
    
take_recommendation(result)