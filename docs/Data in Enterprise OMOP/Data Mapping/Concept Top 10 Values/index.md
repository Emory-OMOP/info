# Concept Top 10 Values

This reference shows the **10 most frequent concept values** for each concept column in every OMOP table, broken down by data source (Enterprise, CDW, Epic). Use it to understand what data is most prevalent and to identify mapping gaps.

!!! tip "How to use this table"
    - **Blank `concept_id`** or **`concept_name`** indicates unmapped source values — the source data exists but isn't mapped to a standard OMOP concept
    - **`concept_id = 0`** means "No matching concept" — the ETL attempted mapping but found no match
    - **`percentage_within_column`** shows how much of the column's total data each concept represents
    - Use this alongside [:octicons-arrow-right-24: Current Concept Coverage](../Current%20Concept%20Coverage/index.md) to assess mapping completeness

---

| schema | tbl_name | col_name | concept_id | total_rows | value_count | percentage_within_column | concept_name  |
| ---|---|---|---|---|---|---|---|
| Enterprise | care_site | place_of_service_concept_id  |  | 36112 | 33077 | 91.6 |  |
| Enterprise | care_site | place_of_service_concept_id  | 8940 | 36112 | 1729 | 4.79 | Office |
| Enterprise | care_site | place_of_service_concept_id  | 8756 | 36112 | 282 | 0.78 | Outpatient Hospital |
| Enterprise | care_site | place_of_service_concept_id  | 8717 | 36112 | 181 | 0.5 | Inpatient Hospital |
| Enterprise | care_site | place_of_service_concept_id  | 0 | 36112 | 163 | 0.45 | No matching concept |
| Enterprise | care_site | place_of_service_concept_id  | 8827 | 36112 | 134 | 0.37 | Custodial Care Facility |
| Enterprise | care_site | place_of_service_concept_id  | 5084 | 36112 | 91 | 0.25 | Off Campus-Outpatient Hospital |
| Enterprise | care_site | place_of_service_concept_id  | 8883 | 36112 | 84 | 0.23 | Ambulatory Surgical Center |
| Enterprise | care_site | place_of_service_concept_id  | 8863 | 36112 | 77 | 0.21 | Skilled Nursing Facility |
| Enterprise | care_site | place_of_service_concept_id  | 8870 | 36112 | 66 | 0.18 | Emergency Room - Hospital |
| Enterprise | condition_occurrence | condition_type_concept_id  | 32019 | 210000000 | 112000000 | 53.29 | EHR billing diagnosis |
| Enterprise | condition_occurrence | condition_status_concept_id  | 32896 | 210000000 | 74121036 | 35.21 | Discharge diagnosis |
| Enterprise | condition_occurrence | condition_status_concept_id  | 32908 | 210000000 | 64584027 | 30.68 | Secondary diagnosis |
| Enterprise | condition_occurrence | condition_type_concept_id  | 32020 | 210000000 | 61826347 | 29.37 | EHR encounter diagnosis |
| Enterprise | condition_occurrence | condition_status_concept_id  | 32902 | 210000000 | 37687166 | 17.91 | Primary diagnosis |
| Enterprise | condition_occurrence | condition_type_concept_id  | 32817 | 210000000 | 17337840 | 8.24 | EHR |
| Enterprise | condition_occurrence | condition_concept_id  | 320128 | 210000000 | 10673701 | 5.07 | Essential hypertension |
| Enterprise | condition_occurrence | condition_status_concept_id  | 32890 | 210000000 | 10428929 | 4.95 | Admission diagnosis |
| Enterprise | condition_occurrence | condition_status_concept_id  |  | 210000000 | 9961804 | 4.73 |  |
| Enterprise | condition_occurrence | condition_source_concept_id  | 35207668 | 210000000 | 8412140 | 4 | Essential (primary) hypertension |
| Enterprise | condition_occurrence | condition_status_concept_id  | 32905 | 210000000 | 8309546 | 3.95 | Referral diagnosis |
| Enterprise | condition_occurrence | condition_type_concept_id  | 42898140 | 210000000 | 8309537 | 3.95 | Referral record |
| Enterprise | condition_occurrence | condition_type_concept_id  | 32840 | 210000000 | 5715222 | 2.72 | EHR problem list |
| Enterprise | condition_occurrence | condition_status_concept_id  | 32901 | 210000000 | 4504390 | 2.14 | Primary admission diagnosis |
| Enterprise | condition_occurrence | condition_type_concept_id  | 44786627 | 210000000 | 3832270 | 1.82 | Primary Condition |
| Enterprise | condition_occurrence | condition_concept_id  | 432867 | 210000000 | 3754203 | 1.78 | Hyperlipidemia |
| Enterprise | condition_occurrence | condition_concept_id  | 4193704 | 210000000 | 3628067 | 1.72 | Type 2 diabetes mellitus without complication |
| Enterprise | condition_occurrence | condition_source_concept_id  | 35206882 | 210000000 | 2651028 | 1.26 | Type 2 diabetes mellitus without complications |
| Enterprise | condition_occurrence | condition_source_concept_id  | 35207065 | 210000000 | 2429626 | 1.15 | Hyperlipidemia, unspecified |
| Enterprise | condition_occurrence | condition_source_concept_id  | 44821949 | 210000000 | 2254375 | 1.07 | Unspecified essential hypertension |
| Enterprise | condition_occurrence | condition_concept_id  | 77670 | 210000000 | 2204634 | 1.05 | Chest pain |
| Enterprise | condition_occurrence | condition_concept_id  | 438720 | 210000000 | 1946858 | 0.92 | Mixed hyperlipidemia |
| Enterprise | condition_occurrence | condition_concept_id  | 764123 | 210000000 | 1888337 | 0.9 | Atherosclerosis of coronary artery without angina pectoris |
| Enterprise | condition_occurrence | condition_source_concept_id  | 45586572 | 210000000 | 1888337 | 0.9 | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| Enterprise | condition_occurrence | condition_concept_id  | 312437 | 210000000 | 1821704 | 0.87 | Dyspnea |
| Enterprise | condition_occurrence | condition_source_concept_id  | 35207062 | 210000000 | 1757807 | 0.84 | Mixed hyperlipidemia |
| Enterprise | condition_occurrence | condition_concept_id  | 201826 | 210000000 | 1671809 | 0.79 | Type 2 diabetes mellitus |
| Enterprise | condition_occurrence | condition_concept_id  | 313217 | 210000000 | 1663920 | 0.79 | Atrial fibrillation |
| Enterprise | condition_occurrence | condition_concept_id  | 42539502 | 210000000 | 1435333 | 0.68 | Transplanted kidney present |
| Enterprise | condition_occurrence | condition_source_concept_id  | 35208190 | 210000000 | 1347360 | 0.64 | Gastro-esophageal reflux disease without esophagitis |
| Enterprise | condition_occurrence | condition_source_concept_id  | 35225404 | 210000000 | 1144971 | 0.54 | Kidney transplant status |
| Enterprise | condition_occurrence | condition_source_concept_id  | 44834715 | 210000000 | 1129591 | 0.54 | Benign essential hypertension |
| Enterprise | condition_occurrence | condition_source_concept_id  | 44827629 | 210000000 | 1070100 | 0.51 | Other and unspecified hyperlipidemia |
| Enterprise | condition_occurrence | condition_type_concept_id  | 38000245 | 210000000 | 1060550 | 0.5 | EHR problem list entry |
| Enterprise | condition_occurrence | condition_status_concept_id  | 32906 | 210000000 | 638479 | 0.3 | Resolved condition |
| Enterprise | condition_occurrence | condition_status_concept_id  | 32907 | 210000000 | 230840 | 0.11 | Secondary admission diagnosis |
| Enterprise | condition_occurrence | condition_type_concept_id  | 44786629 | 210000000 | 230852 | 0.11 | Secondary Condition |
| Enterprise | condition_occurrence | condition_status_concept_id  | 32893 | 210000000 | 7192 | 0 | Confirmed diagnosis |
| Enterprise | device_exposure | device_type_concept_id  | 44818707 | 14334871 | 14334871 | 100 | EHR Detail |
| Enterprise | device_exposure | unit_source_concept_id  |  | 14334871 | 14334871 | 100 |  |
| Enterprise | device_exposure | unit_concept_id  |  | 14334871 | 14334871 | 100 |  |
| Enterprise | device_exposure | device_source_concept_id  |  | 14334871 | 13980295 | 97.53 |  |
| Enterprise | device_exposure | device_concept_id  | 4224038 | 14334871 | 9288310 | 64.8 | Oxygen nasal cannula |
| Enterprise | device_exposure | device_concept_id  | 40493026 | 14334871 | 2525205 | 17.62 | Mechanical ventilator |
| Enterprise | device_exposure | device_concept_id  | 4139525 | 14334871 | 854929 | 5.96 | High flow oxygen nasal cannula |
| Enterprise | device_exposure | device_concept_id  | 45768222 | 14334871 | 337464 | 2.35 | Continuous positive airway pressure/Bilevel positive airway pressure mask |
| Enterprise | device_exposure | device_concept_id  | 4222966 | 14334871 | 313143 | 2.18 | Oxygen mask |
| Enterprise | device_exposure | device_concept_id  | 4138916 | 14334871 | 248856 | 1.74 | Oxygen ventilator |
| Enterprise | device_exposure | device_concept_id  | 45771595 | 14334871 | 162318 | 1.13 | Non-rebreathing oxygen face mask |
| Enterprise | device_exposure | device_concept_id  | 4145528 | 14334871 | 158140 | 1.1 | Nonrebreather oxygen mask |
| Enterprise | device_exposure | device_concept_id  | 4322904 | 14334871 | 42992 | 0.3 | Venturi mask |
| Enterprise | device_exposure | device_concept_id  | 2211851 | 14334871 | 40462 | 0.28 | Treatment devices, design and construction; complex (irregular blocks, special shields, compensators, wedges, molds or casts) |
| Enterprise | device_exposure | device_source_concept_id  | 2211851 | 14334871 | 40462 | 0.28 | Treatment devices, design and construction; complex (irregular blocks, special shields, compensators, wedges, molds or casts) |
| Enterprise | device_exposure | device_source_concept_id  | 2721881 | 14334871 | 25187 | 0.18 | Posterior chamber intraocular lens |
| Enterprise | device_exposure | device_source_concept_id  | 2615740 | 14334871 | 17127 | 0.12 | Anchor/screw for opposing bone-to-bone or soft tissue-to-bone (implantable) |
| Enterprise | device_exposure | device_source_concept_id  | 2721868 | 14334871 | 14816 | 0.1 | Contact lens, other type |
| Enterprise | device_exposure | device_source_concept_id  | 2616666 | 14334871 | 14163 | 0.1 | Continuous positive airway pressure (cpap) device |
| Enterprise | device_exposure | device_source_concept_id  | 2615322 | 14334871 | 13083 | 0.09 | Technetium tc-99m sestamibi, diagnostic, per study dose |
| Enterprise | device_exposure | device_source_concept_id  | 2721783 | 14334871 | 11819 | 0.08 | Frames, purchases |
| Enterprise | device_exposure | device_source_concept_id  | 2720870 | 14334871 | 11300 | 0.08 | Low osmolar contrast material, 300-399 mg/ml iodine concentration, per ml |
| Enterprise | device_exposure | device_source_concept_id  | 2615268 | 14334871 | 10498 | 0.07 | Filter, disposable, used with positive airway pressure device |
| Enterprise | drug_exposure | drug_source_concept_id  |  | 307000000 | 292000000 | 95.03 |  |
| Enterprise | drug_exposure | drug_type_concept_id  | 38000180 | 307000000 | 234000000 | 76 | Inpatient administration |
| Enterprise | drug_exposure | route_concept_id  | 4171047 | 307000000 | 112000000 | 36.43 | Intravenous |
| Enterprise | drug_exposure | route_concept_id  | 4132161 | 307000000 | 78709292 | 25.61 | Oral |
| Enterprise | drug_exposure | route_concept_id  |  | 307000000 | 71935478 | 23.41 |  |
| Enterprise | drug_exposure | drug_type_concept_id  | 38000177 | 307000000 | 58383170 | 19 | Prescription written |
| Enterprise | drug_exposure | drug_concept_id  | 19079524 | 307000000 | 21843837 | 7.11 | sodium chloride 9 MG/ML Injectable Solution |
| Enterprise | drug_exposure | drug_concept_id  | 967823 | 307000000 | 14950591 | 4.86 | sodium chloride |
| Enterprise | drug_exposure | drug_concept_id  | 19097059 | 307000000 | 13962209 | 4.54 | DEXTROSE SOLUTION |
| Enterprise | drug_exposure | route_concept_id  | 4142048 | 307000000 | 13887679 | 4.52 | Subcutaneous |
| Enterprise | drug_exposure | drug_type_concept_id  | 32817 | 307000000 | 13162088 | 4.28 | EHR |
| Enterprise | drug_exposure | route_concept_id  | 0 | 307000000 | 13162088 | 4.28 | No matching concept |
| Enterprise | drug_exposure | drug_concept_id  | 19076324 | 307000000 | 11924660 | 3.88 | glucose 50 MG/ML Injectable Solution |
| Enterprise | drug_exposure | drug_concept_id  | 1154186 | 307000000 | 5798694 | 1.89 | fentanyl 0.1 MG |
| Enterprise | drug_exposure | drug_concept_id  | 1718370 | 307000000 | 5482346 | 1.78 | heparin Injectable Solution |
| Enterprise | drug_exposure | route_concept_id  | 45956874 | 307000000 | 5207800 | 1.69 | Inhalation |
| Enterprise | drug_exposure | drug_concept_id  | 19135374 | 307000000 | 5096597 | 1.66 | calcium chloride 0.2 MG/ML / potassium chloride 0.3 MG/ML / sodium chloride 6 MG/ML / sodium lactate 3.1 MG/ML Injectable Solution |
| Enterprise | drug_exposure | route_concept_id  | 4263689 | 307000000 | 3934835 | 1.28 | Topical |
| Enterprise | drug_exposure | drug_concept_id  | 19122121 | 307000000 | 3817175 | 1.24 | Insulin |
| Enterprise | drug_exposure | drug_concept_id  | 1321341 | 307000000 | 3573456 | 1.16 | norepinephrine |
| Enterprise | drug_exposure | drug_concept_id  | 1127433 | 307000000 | 3235619 | 1.05 | acetaminophen 325 MG Oral Tablet |
| Enterprise | drug_exposure | drug_type_concept_id  | 38000179 | 307000000 | 2102094 | 0.68 | Physician administered drug (identified as procedure) |
| Enterprise | drug_exposure | route_concept_id  | 4132711 | 307000000 | 1942551 | 0.63 | Nasogastric |
| Enterprise | drug_exposure | route_concept_id  | 4303795 | 307000000 | 1805196 | 0.59 | Orogastric |
| Enterprise | drug_exposure | route_concept_id  | 40549429 | 307000000 | 1711381 | 0.56 | Ocular |
| Enterprise | drug_exposure | drug_source_concept_id  | 1537215 | 307000000 | 516370 | 0.17 | propofol lipid emulsion |
| Enterprise | drug_exposure | drug_source_concept_id  | 46275280 | 307000000 | 360926 | 0.12 | 50 ML magnesium sulfate 40 MG/ML Injection |
| Enterprise | drug_exposure | drug_source_concept_id  | 19052492 | 307000000 | 356787 | 0.12 | phenylephrine tannate |
| Enterprise | drug_exposure | drug_source_concept_id  | 46274317 | 307000000 | 249106 | 0.08 | lidocaine hydrochloride anhydrous |
| Enterprise | drug_exposure | drug_source_concept_id  | 19080985 | 307000000 | 241058 | 0.08 | iohexol |
| Enterprise | drug_exposure | drug_source_concept_id  | 44784902 | 307000000 | 230060 | 0.07 | potassium chloride 20 MEQ Extended Release Oral Tablet [K-Tab] |
| Enterprise | drug_exposure | drug_source_concept_id  | 42707668 | 307000000 | 222642 | 0.07 | acetaminophen 325 MG Oral Tablet [Ringl] |
| Enterprise | drug_exposure | drug_source_concept_id  | 19082873 | 307000000 | 220490 | 0.07 | rocuronium bromide |
| Enterprise | drug_exposure | drug_source_concept_id  | 2617177 | 307000000 | 182821 | 0.06 | Administration of influenza virus vaccine |
| Enterprise | drug_exposure | drug_type_concept_id  | 38000175 | 307000000 | 110463 | 0.04 | Prescription dispensed in pharmacy |
| Enterprise | location | country_concept_id  | -99 | 5031674 | 5031082 | 99.99 |  |
| Enterprise | location | country_concept_id  |  | 5031674 | 592 | 0.01 |  |
| Enterprise | measurement | meas_event_field_concept_id  |  | 1040000000 | 1040000000 | 100 |  |
| Enterprise | measurement | unit_source_concept_id  |  | 1040000000 | 1040000000 | 100 |  |
| Enterprise | measurement | operator_concept_id  | 4172703 | 1040000000 | 962000000 | 92.16 | = |
| Enterprise | measurement | measurement_source_concept_id  |  | 1040000000 | 903000000 | 86.56 |  |
| Enterprise | measurement | value_as_concept_id  |  | 1040000000 | 900000000 | 86.24 |  |
| Enterprise | measurement | measurement_type_concept_id  | 44818701 | 1040000000 | 594000000 | 56.91 | From physical examination |
| Enterprise | measurement | measurement_type_concept_id  | 44818702 | 1040000000 | 317000000 | 30.37 | Lab result |
| Enterprise | measurement | unit_concept_id  | 8876 | 1040000000 | 179000000 | 17.15 | millimeter mercury column |
| Enterprise | measurement | unit_concept_id  | 0 | 1040000000 | 130000000 | 12.41 | No matching concept |
| Enterprise | measurement | value_as_concept_id  | 0 | 1040000000 | 130000000 | 12.41 | No matching concept |
| Enterprise | measurement | measurement_type_concept_id  | 32817 | 1040000000 | 130000000 | 12.41 | EHR |
| Enterprise | measurement | unit_concept_id  | 8554 | 1040000000 | 107000000 | 10.22 | percent |
| Enterprise | measurement | unit_concept_id  |  | 1040000000 | 93310128 | 8.94 |  |
| Enterprise | measurement | measurement_concept_id  | 3027018 | 1040000000 | 78317465 | 7.51 | Heart rate |
| Enterprise | measurement | unit_concept_id  | 4118124 | 1040000000 | 78083741 | 7.48 | beats/min |
| Enterprise | measurement | operator_concept_id  |  | 1040000000 | 76526643 | 7.34 |  |
| Enterprise | measurement | measurement_concept_id  | 3004249 | 1040000000 | 71826962 | 6.88 | Systolic blood pressure |
| Enterprise | measurement | measurement_concept_id  | 3012888 | 1040000000 | 71743572 | 6.88 | Diastolic blood pressure |
| Enterprise | measurement | measurement_concept_id  | 3024171 | 1040000000 | 69634036 | 6.67 | Respiratory rate |
| Enterprise | measurement | measurement_concept_id  | 40762499 | 1040000000 | 68467946 | 6.56 | Oxygen saturation in Arterial blood by Pulse oximetry |
| Enterprise | measurement | unit_concept_id  | 4117833 | 1040000000 | 66081048 | 6.33 | breaths/min |
| Enterprise | measurement | unit_concept_id  | 8840 | 1040000000 | 65640705 | 6.29 | milligram per deciliter |
| Enterprise | measurement | measurement_concept_id  | 3020891 | 1040000000 | 44223560 | 4.24 | Body temperature |
| Enterprise | measurement | unit_concept_id  | 586323 | 1040000000 | 43471174 | 4.17 | degree Celsius |
| Enterprise | measurement | unit_concept_id  | 8753 | 1040000000 | 42150843 | 4.04 | millimole per liter |
| Enterprise | measurement | measurement_concept_id  | 3027598 | 1040000000 | 36944486 | 3.54 | Mean blood pressure |
| Enterprise | measurement | unit_concept_id  | 8848 | 1040000000 | 32990152 | 3.16 | thousand per microliter |
| Enterprise | measurement | measurement_concept_id  | 3025315 | 1040000000 | 18749281 | 1.8 | Body weight |
| Enterprise | measurement | measurement_concept_id  | 3005424 | 1040000000 | 18450763 | 1.77 | Body surface area |
| Enterprise | measurement | measurement_concept_id  | 3038553 | 1040000000 | 17360285 | 1.66 | Body mass index (BMI) [Ratio] |
| Enterprise | measurement | value_as_concept_id  | 9189 | 1040000000 | 12125433 | 1.16 | Negative |
| Enterprise | measurement | operator_concept_id  | 4171756 | 1040000000 | 4604500 | 0.44 | < |
| Enterprise | measurement | measurement_source_concept_id  | 3000483 | 1040000000 | 3691268 | 0.35 | Glucose [Mass/volume] in Blood |
| Enterprise | measurement | measurement_type_concept_id  | 5001 | 1040000000 | 3223118 | 0.31 | Test ordered through EHR |
| Enterprise | measurement | measurement_source_concept_id  | 3023103 | 1040000000 | 3151373 | 0.3 | Potassium [Moles/volume] in Serum or Plasma |
| Enterprise | measurement | measurement_source_concept_id  | 3019550 | 1040000000 | 3104215 | 0.3 | Sodium [Moles/volume] in Serum or Plasma |
| Enterprise | measurement | measurement_source_concept_id  | 3006906 | 1040000000 | 3053426 | 0.29 | Calcium [Mass/volume] in Serum or Plasma |
| Enterprise | measurement | measurement_source_concept_id  | 3004501 | 1040000000 | 3053073 | 0.29 | Glucose [Mass/volume] in Serum or Plasma |
| Enterprise | measurement | measurement_source_concept_id  | 3008295 | 1040000000 | 3022633 | 0.29 | Osmolality of Serum or Plasma |
| Enterprise | measurement | measurement_source_concept_id  | 3045716 | 1040000000 | 3013324 | 0.29 | Anion gap in Serum or Plasma |
| Enterprise | measurement | measurement_source_concept_id  | 3000963 | 1040000000 | 2977029 | 0.29 | Hemoglobin [Mass/volume] in Blood |
| Enterprise | measurement | measurement_source_concept_id  | 3024929 | 1040000000 | 2878119 | 0.28 | Platelets [#/volume] in Blood by Automated count |
| Enterprise | measurement | value_as_concept_id  | 9191 | 1040000000 | 1507426 | 0.14 | Positive |
| Enterprise | measurement | operator_concept_id  | 4172704 | 1040000000 | 448873 | 0.04 | > |
| Enterprise | measurement | value_as_concept_id  | 4135493 | 1040000000 | 325699 | 0.03 | Abnormal |
| Enterprise | measurement | operator_concept_id  | 4171755 | 1040000000 | 161427 | 0.02 | >= |
| Enterprise | measurement | operator_concept_id  | 4171754 | 1040000000 | 334 | 0 | <= |
| Enterprise | measurement | value_as_concept_id  | 4084765 | 1040000000 | 34098 | 0 | Above reference range |
| Enterprise | measurement | value_as_concept_id  | 4167406 | 1040000000 | 9914 | 0 | Eye disorder screening |
| Enterprise | measurement | value_as_concept_id  | 37311061 | 1040000000 | 497 | 0 | COVID-19 |
| Enterprise | measurement | value_as_concept_id  | 4116822 | 1040000000 | 261 | 0 | Unsatisfactory |
| Enterprise | measurement | value_as_concept_id  | 4169782 | 1040000000 | 98 | 0 | Inconclusive |
| Enterprise | observation | obs_event_field_concept_id  |  | 2560000000 | 2560000000 | 100 |  |
| Enterprise | observation | qualifier_concept_id  | -99 | 2560000000 | 2350000000 | 92 |  |
| Enterprise | observation | unit_concept_id  | -99 | 2560000000 | 2350000000 | 92 |  |
| Enterprise | observation | observation_type_concept_id  | 32817 | 2560000000 | 2350000000 | 92 | EHR |
| Enterprise | observation | observation_concept_id  | 0 | 2560000000 | 2350000000 | 91.92 | No matching concept |
| Enterprise | observation | observation_source_concept_id  | 0 | 2560000000 | 2350000000 | 91.89 | No matching concept |
| Enterprise | observation | value_as_concept_id  | 0 | 2560000000 | 2350000000 | 91.87 | No matching concept |
| Enterprise | observation | qualifier_concept_id  |  | 2560000000 | 205000000 | 8 |  |
| Enterprise | observation | observation_type_concept_id  | 38000280 | 2560000000 | 205000000 | 7.99 | Observation recorded from EHR |
| Enterprise | observation | unit_concept_id  |  | 2560000000 | 193000000 | 7.53 |  |
| Enterprise | observation | value_as_concept_id  |  | 2560000000 | 167000000 | 6.53 |  |
| Enterprise | observation | observation_source_concept_id  |  | 2560000000 | 155000000 | 6.07 |  |
| Enterprise | observation | observation_concept_id  | 4022240 | 2560000000 | 36936284 | 1.44 | Pain score |
| Enterprise | observation | observation_concept_id  | 4249118 | 2560000000 | 17512004 | 0.68 | Reason for visit diagnosis |
| Enterprise | observation | observation_concept_id  | 4268843 | 2560000000 | 15481963 | 0.61 | Finding of tobacco use and exposure |
| Enterprise | observation | observation_concept_id  | 4267143 | 2560000000 | 9593807 | 0.37 | Language |
| Enterprise | observation | observation_concept_id  | 4267504 | 2560000000 | 9593796 | 0.37 | Finding of marital or partnership status |
| Enterprise | observation | observation_concept_id  | 4084277 | 2560000000 | 8315630 | 0.33 | Glasgow Coma Score eye opening subscore |
| Enterprise | observation | value_as_concept_id  | 4144272 | 2560000000 | 8366056 | 0.33 | Never smoked tobacco |
| Enterprise | observation | observation_concept_id  | 4084912 | 2560000000 | 8308958 | 0.32 | Glasgow Coma Scale verbal response subscore |
| Enterprise | observation | observation_concept_id  | 4083352 | 2560000000 | 8295394 | 0.32 | Glasgow Coma Scale motor response subscore |
| Enterprise | observation | observation_concept_id  | 4093836 | 2560000000 | 8166688 | 0.32 | Glasgow coma score |
| Enterprise | observation | unit_concept_id  | 8876 | 2560000000 | 7745241 | 0.3 | millimeter mercury column |
| Enterprise | observation | value_as_concept_id  | 4151757 | 2560000000 | 6453892 | 0.25 | Main spoken language English |
| Enterprise | observation | observation_source_concept_id  | 2414398 | 2560000000 | 5587840 | 0.22 | Office or other outpatient visit for the evaluation and management of an established patient, which requires a medically appropriate history and/or examination and moderate level of medical decision making. When using total time on the date of the enco... |
| Enterprise | observation | observation_source_concept_id  | 2414397 | 2560000000 | 4032312 | 0.16 | Office or other outpatient visit for the evaluation and management of an established patient, which requires a medically appropriate history and/or examination and low level of medical decision making. When using total time on the date of the encounter... |
| Enterprise | observation | value_as_concept_id  | 4338692 | 2560000000 | 3539167 | 0.14 | Married |
| Enterprise | observation | value_as_concept_id  | 4310250 | 2560000000 | 3397316 | 0.13 | Ex-smoker |
| Enterprise | observation | observation_source_concept_id  | 45537679 | 2560000000 | 3160608 | 0.12 | Other long term (current) drug therapy |
| Enterprise | observation | unit_concept_id  | 8587 | 2560000000 | 2634075 | 0.1 | milliliter |
| Enterprise | observation | value_as_concept_id  | 4053842 | 2560000000 | 2674769 | 0.1 | Single person |
| Enterprise | observation | unit_concept_id  | 4117833 | 2560000000 | 1753879 | 0.07 | breaths/min |
| Enterprise | observation | value_as_concept_id  | 4276526 | 2560000000 | 1906303 | 0.07 | Cigarette smoker |
| Enterprise | observation | observation_source_concept_id  | 45552108 | 2560000000 | 1239997 | 0.05 | Long term (current) use of anticoagulants |
| Enterprise | observation | observation_source_concept_id  | 2414345 | 2560000000 | 1040755 | 0.04 | Postoperative follow-up visit, normally included in the surgical package, to indicate that an evaluation and management service was performed during a postoperative period for a reason(s) related to the original procedure |
| Enterprise | observation | observation_source_concept_id  | 2414393 | 2560000000 | 903519 | 0.04 | Office or other outpatient visit for the evaluation and management of a new patient, which requires a medically appropriate history and/or examination and moderate level of medical decision making. When using total time on the date of the encounter for... |
| Enterprise | observation | observation_source_concept_id  | 37202304 | 2560000000 | 799687 | 0.03 | Other specified postprocedural states |
| Enterprise | observation | observation_source_concept_id  | 45534458 | 2560000000 | 767248 | 0.03 | Other fatigue |
| Enterprise | observation | value_as_concept_id  | 42709996 | 2560000000 | 884034 | 0.03 | Smokes tobacco daily |
| Enterprise | observation | value_as_concept_id  | 1340204 | 2560000000 | 723312 | 0.03 | History of event |
| Enterprise | observation | observation_type_concept_id  | 581413 | 2560000000 | 262828 | 0.01 | Observation from Measurement |
| Enterprise | person | race_concept_id  | 0 | 6387709 | 6378672 | 99.86 | No matching concept |
| Enterprise | person | ethnicity_concept_id  | 0 | 6387709 | 6378156 | 99.85 | No matching concept |
| Enterprise | person | gender_concept_id  | 0 | 6387709 | 6260487 | 98.01 | No matching concept |
| Enterprise | person | race_source_concept_id  | -99 | 6387709 | 6258439 | 97.98 |  |
| Enterprise | person | ethnicity_source_concept_id  | -99 | 6387709 | 6258439 | 97.98 |  |
| Enterprise | person | gender_source_concept_id  | -99 | 6387709 | 6258439 | 97.98 |  |
| Enterprise | person | race_source_concept_id  |  | 6387709 | 129270 | 2.02 |  |
| Enterprise | person | ethnicity_source_concept_id  |  | 6387709 | 129270 | 2.02 |  |
| Enterprise | person | gender_source_concept_id  |  | 6387709 | 129270 | 2.02 |  |
| Enterprise | person | gender_concept_id  | 8532 | 6387709 | 82592 | 1.29 | FEMALE |
| Enterprise | person | gender_concept_id  | 8507 | 6387709 | 44630 | 0.7 | MALE |
| Enterprise | person | ethnicity_concept_id  | 38003564 | 6387709 | 8742 | 0.14 | Not Hispanic or Latino |
| Enterprise | person | race_concept_id  | 8516 | 6387709 | 5505 | 0.09 | Black or African American |
| Enterprise | person | race_concept_id  | 8527 | 6387709 | 3064 | 0.05 | White |
| Enterprise | person | race_concept_id  | 8515 | 6387709 | 384 | 0.01 | Asian |
| Enterprise | person | ethnicity_concept_id  | 38003563 | 6387709 | 811 | 0.01 | Hispanic or Latino |
| Enterprise | person | race_concept_id  | 8557 | 6387709 | 48 | 0 | Native Hawaiian or Other Pacific Islander |
| Enterprise | person | race_concept_id  | 8657 | 6387709 | 36 | 0 | American Indian or Alaska Native |
| Enterprise | procedure_occurrence | modifier_concept_id  |  | 51555514 | 41868731 | 81.21 |  |
| Enterprise | procedure_occurrence | procedure_type_concept_id  | 44786630 | 51555514 | 28713807 | 55.69 | Primary Procedure |
| Enterprise | procedure_occurrence | procedure_type_concept_id  | 42865906 | 51555514 | 11180331 | 21.69 | Condition Procedure |
| Enterprise | procedure_occurrence | procedure_type_concept_id  | 32817 | 51555514 | 9686783 | 18.79 | EHR |
| Enterprise | procedure_occurrence | modifier_concept_id  | 0 | 51555514 | 9469003 | 18.37 | No matching concept |
| Enterprise | procedure_occurrence | procedure_concept_id  | 4036803 | 51555514 | 2356868 | 4.57 | General examination of patient |
| Enterprise | procedure_occurrence | procedure_source_concept_id  | 2514409 | 51555514 | 2006738 | 3.89 | Subsequent hospital inpatient or observation care, per day, for the evaluation and management of a patient, which requires a medically appropriate history and/or examination and high level of medical decision making. When using total time on the date o... |
| Enterprise | procedure_occurrence | procedure_concept_id  | 2514409 | 51555514 | 2006738 | 3.89 | Subsequent hospital inpatient or observation care, per day, for the evaluation and management of a patient, which requires a medically appropriate history and/or examination and high level of medical decision making. When using total time on the date o... |
| Enterprise | procedure_occurrence | procedure_type_concept_id  | 44786631 | 51555514 | 1974593 | 3.83 | Secondary Procedure |
| Enterprise | procedure_occurrence | procedure_source_concept_id  | 45552054 | 51555514 | 1653407 | 3.21 | Encounter for general adult medical examination without abnormal findings |
| Enterprise | procedure_occurrence | procedure_source_concept_id  | 2313816 | 51555514 | 1652723 | 3.21 | Electrocardiogram, routine ECG with at least 12 leads; interpretation and report only |
| Enterprise | procedure_occurrence | procedure_concept_id  | 2313816 | 51555514 | 1652723 | 3.21 | Electrocardiogram, routine ECG with at least 12 leads; interpretation and report only |
| Enterprise | procedure_occurrence | procedure_source_concept_id  | 2313814 | 51555514 | 1472204 | 2.86 | Electrocardiogram, routine ECG with at least 12 leads; with interpretation and report |
| Enterprise | procedure_occurrence | procedure_concept_id  | 2313814 | 51555514 | 1472204 | 2.86 | Electrocardiogram, routine ECG with at least 12 leads; with interpretation and report |
| Enterprise | procedure_occurrence | procedure_source_concept_id  | 2514408 | 51555514 | 1342543 | 2.6 | Subsequent hospital inpatient or observation care, per day, for the evaluation and management of a patient, which requires a medically appropriate history and/or examination and moderate level of medical decision making. When using total time on the da... |
| Enterprise | procedure_occurrence | procedure_concept_id  | 2514408 | 51555514 | 1342543 | 2.6 | Subsequent hospital inpatient or observation care, per day, for the evaluation and management of a patient, which requires a medically appropriate history and/or examination and moderate level of medical decision making. When using total time on the da... |
| Enterprise | procedure_occurrence | procedure_source_concept_id  | 725068 | 51555514 | 1109503 | 2.15 | Radiologic examination, chest; single view |
| Enterprise | procedure_occurrence | procedure_concept_id  | 725068 | 51555514 | 1109503 | 2.15 | Radiologic examination, chest; single view |
| Enterprise | procedure_occurrence | procedure_source_concept_id  | 44828573 | 51555514 | 912430 | 1.77 | Long-term (current) use of other medications |
| Enterprise | procedure_occurrence | procedure_concept_id  | 4141759 | 51555514 | 912430 | 1.77 | Long-term drug therapy |
| Enterprise | procedure_occurrence | procedure_source_concept_id  | 35225097 | 51555514 | 909718 | 1.76 | Encounter for immunization |
| Enterprise | procedure_occurrence | procedure_concept_id  | 4132855 | 51555514 | 909718 | 1.76 | Active or passive immunization |
| Enterprise | procedure_occurrence | procedure_source_concept_id  | 2514441 | 51555514 | 778046 | 1.51 | Critical care, evaluation and management of the critically ill or critically injured patient; first 30-74 minutes |
| Enterprise | procedure_occurrence | procedure_concept_id  | 2514441 | 51555514 | 778046 | 1.51 | Critical care, evaluation and management of the critically ill or critically injured patient; first 30-74 minutes |
| Enterprise | procedure_occurrence | procedure_source_concept_id  | 44826243 | 51555514 | 615030 | 1.19 | Routine general medical examination at a health care facility |
| Enterprise | procedure_occurrence | procedure_concept_id  | 36713195 | 51555514 | 582214 | 1.13 | Plain X-ray of chest, anteroposterior view |
| Enterprise | procedure_occurrence | modifier_concept_id  | -99 | 51555514 | 217780 | 0.42 |  |
| Enterprise | provider | specialty_concept_id  | 0 | 403049 | 360290 | 89.39 | No matching concept |
| Enterprise | provider | specialty_source_concept_id  |  | 403049 | 325513 | 80.76 |  |
| Enterprise | provider | gender_source_concept_id  |  | 403049 | 325513 | 80.76 |  |
| Enterprise | provider | gender_concept_id  |  | 403049 | 325513 | 80.76 |  |
| Enterprise | provider | specialty_source_concept_id  | -99 | 403049 | 77536 | 19.24 |  |
| Enterprise | provider | gender_source_concept_id  | -99 | 403049 | 77536 | 19.24 |  |
| Enterprise | provider | gender_concept_id  | -99 | 403049 | 77536 | 19.24 |  |
| Enterprise | provider | specialty_concept_id  | 38004456 | 403049 | 6781 | 1.68 | Internal Medicine |
| Enterprise | provider | specialty_concept_id  | 38003851 | 403049 | 4633 | 1.15 | Family Medicine |
| Enterprise | provider | specialty_concept_id  | 38004510 | 403049 | 3196 | 0.79 | Emergency Medicine |
| Enterprise | provider | specialty_concept_id  | 38004451 | 403049 | 2570 | 0.64 | Cardiology |
| Enterprise | provider | specialty_concept_id  | 38004447 | 403049 | 2365 | 0.59 | General Surgery |
| Enterprise | provider | specialty_concept_id  | 38004450 | 403049 | 2341 | 0.58 | Anesthesiology |
| Enterprise | provider | specialty_concept_id  | 45756825 | 403049 | 1833 | 0.45 | Radiology |
| Enterprise | provider | specialty_concept_id  | 38004461 | 403049 | 1060 | 0.26 | Obstetrics / Gynecology |
| Enterprise | provider | specialty_concept_id  | 38004458 | 403049 | 962 | 0.24 | Neurology |
| Enterprise | visit_detail | visit_detail_source_concept_id  |  | 31784184 | 31784184 | 100 |  |
| Enterprise | visit_detail | visit_detail_type_concept_id  | 32035 | 31784184 | 27454991 | 86.38 | Visit derived from EHR encounter record |
| Enterprise | visit_detail | visit_detail_concept_id  | 9201 | 31784184 | 27454991 | 86.38 | Inpatient Visit |
| Enterprise | visit_detail | admitted_from_concept_id  |  | 31784184 | 27454991 | 86.38 |  |
| Enterprise | visit_detail | visit_detail_type_concept_id  | 44818518 | 31784184 | 4329193 | 13.62 | Visit derived from EHR record |
| Enterprise | visit_detail | visit_detail_concept_id  | 0 | 31784184 | 4329193 | 13.62 | No matching concept |
| Enterprise | visit_detail | admitted_from_concept_id  | 0 | 31784184 | 4329193 | 13.62 | No matching concept |
| CDW | care_site | place_of_service_concept_id  |  | 35949 | 33077 | 92.01 |  |
| CDW | care_site | place_of_service_concept_id  | 8940 | 35949 | 1729 | 4.81 | Office |
| CDW | care_site | place_of_service_concept_id  | 8756 | 35949 | 282 | 0.78 | Outpatient Hospital |
| CDW | care_site | place_of_service_concept_id  | 8717 | 35949 | 181 | 0.5 | Inpatient Hospital |
| CDW | care_site | place_of_service_concept_id  | 8827 | 35949 | 134 | 0.37 | Custodial Care Facility |
| CDW | care_site | place_of_service_concept_id  | 5084 | 35949 | 91 | 0.25 | Off Campus-Outpatient Hospital |
| CDW | care_site | place_of_service_concept_id  | 8883 | 35949 | 84 | 0.23 | Ambulatory Surgical Center |
| CDW | care_site | place_of_service_concept_id  | 8863 | 35949 | 77 | 0.21 | Skilled Nursing Facility |
| CDW | care_site | place_of_service_concept_id  | 8870 | 35949 | 66 | 0.18 | Emergency Room - Hospital |
| CDW | care_site | place_of_service_concept_id  | 8676 | 35949 | 63 | 0.18 | Nursing Facility |
| CDW | condition_occurrence | condition_type_concept_id  | 32019 | 177000000 | 102000000 | 57.49 | EHR billing diagnosis |
| CDW | condition_occurrence | condition_status_concept_id  | 32908 | 177000000 | 64584027 | 36.48 | Secondary diagnosis |
| CDW | condition_occurrence | condition_type_concept_id  | 32020 | 177000000 | 61826347 | 34.92 | EHR encounter diagnosis |
| CDW | condition_occurrence | condition_status_concept_id  | 32896 | 177000000 | 46399433 | 26.21 | Discharge diagnosis |
| CDW | condition_occurrence | condition_status_concept_id  | 32902 | 177000000 | 37687166 | 21.29 | Primary diagnosis |
| CDW | condition_occurrence | condition_status_concept_id  | 32890 | 177000000 | 10428929 | 5.89 | Admission diagnosis |
| CDW | condition_occurrence | condition_concept_id  | 320128 | 177000000 | 9002539 | 5.08 | Essential hypertension |
| CDW | condition_occurrence | condition_status_concept_id  | 32905 | 177000000 | 8309546 | 4.69 | Referral diagnosis |
| CDW | condition_occurrence | condition_type_concept_id  | 42898140 | 177000000 | 8309537 | 4.69 | Referral record |
| CDW | condition_occurrence | condition_source_concept_id  | 35207668 | 177000000 | 6740978 | 3.81 | Essential (primary) hypertension |
| CDW | condition_occurrence | condition_status_concept_id  |  | 177000000 | 4843683 | 2.74 |  |
| CDW | condition_occurrence | condition_status_concept_id  | 32901 | 177000000 | 4504390 | 2.54 | Primary admission diagnosis |
| CDW | condition_occurrence | condition_type_concept_id  | 44786627 | 177000000 | 3832270 | 2.16 | Primary Condition |
| CDW | condition_occurrence | condition_concept_id  | 432867 | 177000000 | 3218429 | 1.82 | Hyperlipidemia |
| CDW | condition_occurrence | condition_concept_id  | 4193704 | 177000000 | 3146655 | 1.78 | Type 2 diabetes mellitus without complication |
| CDW | condition_occurrence | condition_source_concept_id  | 44821949 | 177000000 | 2254375 | 1.27 | Unspecified essential hypertension |
| CDW | condition_occurrence | condition_source_concept_id  | 35206882 | 177000000 | 2169616 | 1.23 | Type 2 diabetes mellitus without complications |
| CDW | condition_occurrence | condition_concept_id  | 77670 | 177000000 | 2012490 | 1.14 | Chest pain |
| CDW | condition_occurrence | condition_source_concept_id  | 35207065 | 177000000 | 1948171 | 1.1 | Hyperlipidemia, unspecified |
| CDW | condition_occurrence | condition_concept_id  | 312437 | 177000000 | 1614822 | 0.91 | Dyspnea |
| CDW | condition_occurrence | condition_source_concept_id  | 45586572 | 177000000 | 1561392 | 0.88 | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| CDW | condition_occurrence | condition_concept_id  | 764123 | 177000000 | 1561392 | 0.88 | Atherosclerosis of coronary artery without angina pectoris |
| CDW | condition_occurrence | condition_concept_id  | 313217 | 177000000 | 1541229 | 0.87 | Atrial fibrillation |
| CDW | condition_occurrence | condition_concept_id  | 438720 | 177000000 | 1432958 | 0.81 | Mixed hyperlipidemia |
| CDW | condition_occurrence | condition_source_concept_id  | 35207062 | 177000000 | 1243907 | 0.7 | Mixed hyperlipidemia |
| CDW | condition_occurrence | condition_concept_id  | 42539502 | 177000000 | 1246239 | 0.7 | Transplanted kidney present |
| CDW | condition_occurrence | condition_concept_id  | 319835 | 177000000 | 1195319 | 0.68 | Congestive heart failure |
| CDW | condition_occurrence | condition_source_concept_id  | 44834715 | 177000000 | 1129591 | 0.64 | Benign essential hypertension |
| CDW | condition_occurrence | condition_source_concept_id  | 44827629 | 177000000 | 1070100 | 0.6 | Other and unspecified hyperlipidemia |
| CDW | condition_occurrence | condition_type_concept_id  | 38000245 | 177000000 | 1060550 | 0.6 | EHR problem list entry |
| CDW | condition_occurrence | condition_source_concept_id  | 35208190 | 177000000 | 989929 | 0.56 | Gastro-esophageal reflux disease without esophagitis |
| CDW | condition_occurrence | condition_source_concept_id  | 44836914 | 177000000 | 977039 | 0.55 | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| CDW | condition_occurrence | condition_status_concept_id  | 32907 | 177000000 | 230840 | 0.13 | Secondary admission diagnosis |
| CDW | condition_occurrence | condition_type_concept_id  | 44786629 | 177000000 | 230852 | 0.13 | Secondary Condition |
| CDW | condition_occurrence | condition_status_concept_id  | 32906 | 177000000 | 41378 | 0.02 | Resolved condition |
| CDW | condition_occurrence | condition_status_concept_id  | 32893 | 177000000 | 7192 | 0 | Confirmed diagnosis |
| CDW | device_exposure | device_type_concept_id  | 44818707 | 14334871 | 14334871 | 100 | EHR Detail |
| CDW | device_exposure | unit_concept_id  |  | 14334871 | 14334871 | 100 |  |
| CDW | device_exposure | unit_source_concept_id  |  | 14334871 | 14334871 | 100 |  |
| CDW | device_exposure | device_source_concept_id  |  | 14334871 | 13980295 | 97.53 |  |
| CDW | device_exposure | device_concept_id  | 4224038 | 14334871 | 9288310 | 64.8 | Oxygen nasal cannula |
| CDW | device_exposure | device_concept_id  | 40493026 | 14334871 | 2525205 | 17.62 | Mechanical ventilator |
| CDW | device_exposure | device_concept_id  | 4139525 | 14334871 | 854929 | 5.96 | High flow oxygen nasal cannula |
| CDW | device_exposure | device_concept_id  | 45768222 | 14334871 | 337464 | 2.35 | Continuous positive airway pressure/Bilevel positive airway pressure mask |
| CDW | device_exposure | device_concept_id  | 4222966 | 14334871 | 313143 | 2.18 | Oxygen mask |
| CDW | device_exposure | device_concept_id  | 4138916 | 14334871 | 248856 | 1.74 | Oxygen ventilator |
| CDW | device_exposure | device_concept_id  | 45771595 | 14334871 | 162318 | 1.13 | Non-rebreathing oxygen face mask |
| CDW | device_exposure | device_concept_id  | 4145528 | 14334871 | 158140 | 1.1 | Nonrebreather oxygen mask |
| CDW | device_exposure | device_concept_id  | 4322904 | 14334871 | 42992 | 0.3 | Venturi mask |
| CDW | device_exposure | device_source_concept_id  | 2211851 | 14334871 | 40462 | 0.28 | Treatment devices, design and construction; complex (irregular blocks, special shields, compensators, wedges, molds or casts) |
| CDW | device_exposure | device_concept_id  | 2211851 | 14334871 | 40462 | 0.28 | Treatment devices, design and construction; complex (irregular blocks, special shields, compensators, wedges, molds or casts) |
| CDW | device_exposure | device_source_concept_id  | 2721881 | 14334871 | 25187 | 0.18 | Posterior chamber intraocular lens |
| CDW | device_exposure | device_source_concept_id  | 2615740 | 14334871 | 17127 | 0.12 | Anchor/screw for opposing bone-to-bone or soft tissue-to-bone (implantable) |
| CDW | device_exposure | device_source_concept_id  | 2721868 | 14334871 | 14816 | 0.1 | Contact lens, other type |
| CDW | device_exposure | device_source_concept_id  | 2616666 | 14334871 | 14163 | 0.1 | Continuous positive airway pressure (cpap) device |
| CDW | device_exposure | device_source_concept_id  | 2615322 | 14334871 | 13083 | 0.09 | Technetium tc-99m sestamibi, diagnostic, per study dose |
| CDW | device_exposure | device_source_concept_id  | 2721783 | 14334871 | 11819 | 0.08 | Frames, purchases |
| CDW | device_exposure | device_source_concept_id  | 2720870 | 14334871 | 11300 | 0.08 | Low osmolar contrast material, 300-399 mg/ml iodine concentration, per ml |
| CDW | device_exposure | device_source_concept_id  | 2615268 | 14334871 | 10498 | 0.07 | Filter, disposable, used with positive airway pressure device |
| CDW | drug_exposure | drug_source_concept_id  |  | 294000000 | 292000000 | 99.29 |  |
| CDW | drug_exposure | drug_type_concept_id  | 38000180 | 294000000 | 234000000 | 79.4 | Inpatient administration |
| CDW | drug_exposure | route_concept_id  | 4171047 | 294000000 | 112000000 | 38.06 | Intravenous |
| CDW | drug_exposure | route_concept_id  | 4132161 | 294000000 | 78709292 | 26.76 | Oral |
| CDW | drug_exposure | route_concept_id  |  | 294000000 | 71935478 | 24.45 |  |
| CDW | drug_exposure | drug_type_concept_id  | 38000177 | 294000000 | 58383170 | 19.85 | Prescription written |
| CDW | drug_exposure | drug_concept_id  | 19079524 | 294000000 | 21843837 | 7.43 | sodium chloride 9 MG/ML Injectable Solution |
| CDW | drug_exposure | drug_concept_id  | 967823 | 294000000 | 14950590 | 5.08 | sodium chloride |
| CDW | drug_exposure | drug_concept_id  | 19097059 | 294000000 | 13962209 | 4.75 | DEXTROSE SOLUTION |
| CDW | drug_exposure | route_concept_id  | 4142048 | 294000000 | 13887679 | 4.72 | Subcutaneous |
| CDW | drug_exposure | drug_concept_id  | 19076324 | 294000000 | 11924660 | 4.05 | glucose 50 MG/ML Injectable Solution |
| CDW | drug_exposure | drug_concept_id  | 1154186 | 294000000 | 5798694 | 1.97 | fentanyl 0.1 MG |
| CDW | drug_exposure | drug_concept_id  | 1718370 | 294000000 | 5482346 | 1.86 | heparin Injectable Solution |
| CDW | drug_exposure | route_concept_id  | 45956874 | 294000000 | 5207800 | 1.77 | Inhalation |
| CDW | drug_exposure | drug_concept_id  | 19135374 | 294000000 | 4990482 | 1.7 | calcium chloride 0.2 MG/ML / potassium chloride 0.3 MG/ML / sodium chloride 6 MG/ML / sodium lactate 3.1 MG/ML Injectable Solution |
| CDW | drug_exposure | route_concept_id  | 4263689 | 294000000 | 3934835 | 1.34 | Topical |
| CDW | drug_exposure | drug_concept_id  | 19122121 | 294000000 | 3817175 | 1.3 | Insulin |
| CDW | drug_exposure | drug_concept_id  | 1321341 | 294000000 | 3533515 | 1.2 | norepinephrine |
| CDW | drug_exposure | drug_concept_id  | 1127433 | 294000000 | 3235619 | 1.1 | acetaminophen 325 MG Oral Tablet |
| CDW | drug_exposure | drug_type_concept_id  | 38000179 | 294000000 | 2102094 | 0.71 | Physician administered drug (identified as procedure) |
| CDW | drug_exposure | route_concept_id  | 4132711 | 294000000 | 1942551 | 0.66 | Nasogastric |
| CDW | drug_exposure | route_concept_id  | 4303795 | 294000000 | 1805196 | 0.61 | Orogastric |
| CDW | drug_exposure | route_concept_id  | 40549429 | 294000000 | 1711381 | 0.58 | Ocular |
| CDW | drug_exposure | route_concept_id  | 4262914 | 294000000 | 1152052 | 0.39 | Nasal |
| CDW | drug_exposure | drug_source_concept_id  | 2617177 | 294000000 | 182821 | 0.06 | Administration of influenza virus vaccine |
| CDW | drug_exposure | drug_source_concept_id  | 2718335 | 294000000 | 169556 | 0.06 | Injection, methylprednisolone acetate, 40 mg (Deprecated) |
| CDW | drug_exposure | drug_source_concept_id  | 44816520 | 294000000 | 154859 | 0.05 | Influenza virus vaccine, quadrivalent (IIV4), split virus, preservative free, 0.5 mL dosage, for intramuscular use |
| CDW | drug_exposure | drug_type_concept_id  | 38000175 | 294000000 | 110463 | 0.04 | Prescription dispensed in pharmacy |
| CDW | drug_exposure | drug_source_concept_id  | 2213473 | 294000000 | 130133 | 0.04 | Tetanus, diphtheria toxoids and acellular pertussis vaccine (Tdap), when administered to individuals 7 years or older, for intramuscular use |
| CDW | drug_exposure | drug_source_concept_id  | 2718347 | 294000000 | 85252 | 0.03 | Injection, dexamethasone sodium phosphate, 1 mg |
| CDW | drug_exposure | drug_source_concept_id  | 2617178 | 294000000 | 79950 | 0.03 | Administration of pneumococcal vaccine |
| CDW | drug_exposure | drug_source_concept_id  | 2213438 | 294000000 | 74361 | 0.03 | Influenza virus vaccine, trivalent (IIV3), split virus, preservative free, 0.5 mL dosage, for intramuscular use |
| CDW | drug_exposure | drug_source_concept_id  | 2718637 | 294000000 | 67786 | 0.02 | Injection, vitamin b-12 cyanocobalamin, up to 1000 mcg |
| CDW | drug_exposure | drug_source_concept_id  | 2718336 | 294000000 | 61176 | 0.02 | Injection, methylprednisolone acetate, 80 mg (Deprecated) |
| CDW | location | country_concept_id  |  | 592 | 592 | 100 |  |
| CDW | measurement | meas_event_field_concept_id  |  | 914000000 | 914000000 | 100 |  |
| CDW | measurement | unit_source_concept_id  |  | 914000000 | 914000000 | 100 |  |
| CDW | measurement | measurement_source_concept_id  |  | 914000000 | 903000000 | 98.83 |  |
| CDW | measurement | value_as_concept_id  |  | 914000000 | 900000000 | 98.47 |  |
| CDW | measurement | operator_concept_id  | 4172703 | 914000000 | 874000000 | 95.65 | = |
| CDW | measurement | measurement_type_concept_id  | 44818701 | 914000000 | 594000000 | 64.97 | From physical examination |
| CDW | measurement | measurement_type_concept_id  | 44818702 | 914000000 | 317000000 | 34.67 | Lab result |
| CDW | measurement | unit_concept_id  | 8876 | 914000000 | 179000000 | 19.59 | millimeter mercury column |
| CDW | measurement | unit_concept_id  | 8554 | 914000000 | 107000000 | 11.66 | percent |
| CDW | measurement | unit_concept_id  |  | 914000000 | 93310128 | 10.21 |  |
| CDW | measurement | measurement_concept_id  | 3027018 | 914000000 | 78317465 | 8.57 | Heart rate |
| CDW | measurement | unit_concept_id  | 4118124 | 914000000 | 78083741 | 8.55 | beats/min |
| CDW | measurement | measurement_concept_id  | 3004249 | 914000000 | 71826962 | 7.86 | Systolic blood pressure |
| CDW | measurement | measurement_concept_id  | 3012888 | 914000000 | 71743572 | 7.85 | Diastolic blood pressure |
| CDW | measurement | measurement_concept_id  | 3024171 | 914000000 | 69634036 | 7.62 | Respiratory rate |
| CDW | measurement | measurement_concept_id  | 40762499 | 914000000 | 68467946 | 7.49 | Oxygen saturation in Arterial blood by Pulse oximetry |
| CDW | measurement | unit_concept_id  | 4117833 | 914000000 | 66081048 | 7.23 | breaths/min |
| CDW | measurement | unit_concept_id  | 8840 | 914000000 | 65640705 | 7.18 | milligram per deciliter |
| CDW | measurement | measurement_concept_id  | 3020891 | 914000000 | 44223560 | 4.84 | Body temperature |
| CDW | measurement | unit_concept_id  | 586323 | 914000000 | 43471174 | 4.76 | degree Celsius |
| CDW | measurement | unit_concept_id  | 8753 | 914000000 | 42150843 | 4.61 | millimole per liter |
| CDW | measurement | measurement_concept_id  | 3027598 | 914000000 | 36944486 | 4.04 | Mean blood pressure |
| CDW | measurement | operator_concept_id  |  | 914000000 | 35902159 | 3.93 |  |
| CDW | measurement | unit_concept_id  | 8848 | 914000000 | 32990152 | 3.61 | thousand per microliter |
| CDW | measurement | unit_concept_id  | 8587 | 914000000 | 27035753 | 2.96 | milliliter |
| CDW | measurement | measurement_concept_id  | 3025315 | 914000000 | 18749281 | 2.05 | Body weight |
| CDW | measurement | measurement_concept_id  | 3005424 | 914000000 | 18450763 | 2.02 | Body surface area |
| CDW | measurement | measurement_concept_id  | 3038553 | 914000000 | 17360285 | 1.9 | Body mass index (BMI) [Ratio] |
| CDW | measurement | value_as_concept_id  | 9189 | 914000000 | 12125433 | 1.33 | Negative |
| CDW | measurement | operator_concept_id  | 4171756 | 914000000 | 3428925 | 0.38 | < |
| CDW | measurement | measurement_type_concept_id  | 5001 | 914000000 | 3223118 | 0.35 | Test ordered through EHR |
| CDW | measurement | value_as_concept_id  | 9191 | 914000000 | 1507426 | 0.16 | Positive |
| CDW | measurement | measurement_source_concept_id  | 45542403 | 914000000 | 832821 | 0.09 | Encounter for screening mammogram for malignant neoplasm of breast |
| CDW | measurement | measurement_source_concept_id  | 2212731 | 914000000 | 549786 | 0.06 | Prothrombin time |
| CDW | measurement | operator_concept_id  | 4172704 | 914000000 | 348268 | 0.04 | > |
| CDW | measurement | value_as_concept_id  | 4135493 | 914000000 | 325699 | 0.04 | Abnormal |
| CDW | measurement | measurement_source_concept_id  | 45552065 | 914000000 | 407221 | 0.04 | Encounter for screening for malignant neoplasm of colon |
| CDW | measurement | measurement_source_concept_id  | 45558483 | 914000000 | 396076 | 0.04 | Other specified abnormal findings of blood chemistry |
| CDW | measurement | measurement_source_concept_id  | 2212168 | 914000000 | 340102 | 0.04 | Urinalysis, by dip stick or tablet reagent for bilirubin, glucose, hemoglobin, ketones, leukocytes, nitrite, pH, protein, specific gravity, urobilinogen, any number of these constituents; automated, without microscopy |
| CDW | measurement | measurement_source_concept_id  | 35225064 | 914000000 | 322512 | 0.04 | Encounter for screening for infections with a predominantly sexual mode of transmission |
| CDW | measurement | measurement_source_concept_id  | 2212392 | 914000000 | 273070 | 0.03 | Hemoglobin; glycosylated (A1C) |
| CDW | measurement | measurement_source_concept_id  | 35206332 | 914000000 | 264388 | 0.03 | Secondary malignant neoplasm of liver and intrahepatic bile duct |
| CDW | measurement | measurement_source_concept_id  | 45556843 | 914000000 | 256479 | 0.03 | Encounter for therapeutic drug level monitoring |
| CDW | measurement | operator_concept_id  | 4171755 | 914000000 | 48393 | 0.01 | >= |
| CDW | measurement | operator_concept_id  | 4171754 | 914000000 | 152 | 0 | <= |
| CDW | measurement | value_as_concept_id  | 4084765 | 914000000 | 34098 | 0 | Above reference range |
| CDW | measurement | value_as_concept_id  | 4167406 | 914000000 | 9914 | 0 | Eye disorder screening |
| CDW | measurement | value_as_concept_id  | 37311061 | 914000000 | 497 | 0 | COVID-19 |
| CDW | measurement | value_as_concept_id  | 4116822 | 914000000 | 261 | 0 | Unsatisfactory |
| CDW | measurement | value_as_concept_id  | 4169782 | 914000000 | 98 | 0 | Inconclusive |
| CDW | measurement | value_as_concept_id  | 4232000 | 914000000 | 78 | 0 | False positive |
| CDW | observation | qualifier_concept_id  |  | 205000000 | 205000000 | 100 |  |
| CDW | observation | obs_event_field_concept_id  |  | 205000000 | 205000000 | 100 |  |
| CDW | observation | observation_type_concept_id  | 38000280 | 205000000 | 205000000 | 99.87 | Observation recorded from EHR |
| CDW | observation | unit_concept_id  |  | 205000000 | 193000000 | 94.08 |  |
| CDW | observation | value_as_concept_id  |  | 205000000 | 167000000 | 81.53 |  |
| CDW | observation | observation_source_concept_id  |  | 205000000 | 155000000 | 75.89 |  |
| CDW | observation | observation_concept_id  | 4022240 | 205000000 | 36936284 | 18.04 | Pain score |
| CDW | observation | observation_concept_id  | 4249118 | 205000000 | 17512004 | 8.55 | Reason for visit diagnosis |
| CDW | observation | observation_concept_id  | 4268843 | 205000000 | 15481963 | 7.56 | Finding of tobacco use and exposure |
| CDW | observation | observation_concept_id  | 4267143 | 205000000 | 9593807 | 4.68 | Language |
| CDW | observation | observation_concept_id  | 4267504 | 205000000 | 9593796 | 4.68 | Finding of marital or partnership status |
| CDW | observation | value_as_concept_id  | 4144272 | 205000000 | 8366056 | 4.08 | Never smoked tobacco |
| CDW | observation | observation_concept_id  | 4084277 | 205000000 | 8315630 | 4.06 | Glasgow Coma Score eye opening subscore |
| CDW | observation | observation_concept_id  | 4084912 | 205000000 | 8308958 | 4.06 | Glasgow Coma Scale verbal response subscore |
| CDW | observation | observation_concept_id  | 4083352 | 205000000 | 8295394 | 4.05 | Glasgow Coma Scale motor response subscore |
| CDW | observation | observation_concept_id  | 4093836 | 205000000 | 8166688 | 3.99 | Glasgow coma score |
| CDW | observation | observation_concept_id  | 4353938 | 205000000 | 7745489 | 3.78 | End tidal carbon dioxide concentration |
| CDW | observation | unit_concept_id  | 8876 | 205000000 | 7745241 | 3.78 | millimeter mercury column |
| CDW | observation | value_as_concept_id  | 4151757 | 205000000 | 6453892 | 3.15 | Main spoken language English |
| CDW | observation | observation_source_concept_id  | 2414398 | 205000000 | 5587840 | 2.73 | Office or other outpatient visit for the evaluation and management of an established patient, which requires a medically appropriate history and/or examination and moderate level of medical decision making. When using total time on the date of the enco... |
| CDW | observation | observation_source_concept_id  | 2414397 | 205000000 | 4032312 | 1.97 | Office or other outpatient visit for the evaluation and management of an established patient, which requires a medically appropriate history and/or examination and low level of medical decision making. When using total time on the date of the encounter... |
| CDW | observation | value_as_concept_id  | 4338692 | 205000000 | 3539167 | 1.73 | Married |
| CDW | observation | value_as_concept_id  | 4310250 | 205000000 | 3397316 | 1.66 | Ex-smoker |
| CDW | observation | observation_source_concept_id  | 45537679 | 205000000 | 2842821 | 1.39 | Other long term (current) drug therapy |
| CDW | observation | value_as_concept_id  | 4053842 | 205000000 | 2674769 | 1.31 | Single person |
| CDW | observation | unit_concept_id  | 8587 | 205000000 | 2634075 | 1.29 | milliliter |
| CDW | observation | value_as_concept_id  | 4276526 | 205000000 | 1906303 | 0.93 | Cigarette smoker |
| CDW | observation | unit_concept_id  | 4117833 | 205000000 | 1753879 | 0.86 | breaths/min |
| CDW | observation | observation_source_concept_id  | 45552108 | 205000000 | 1088848 | 0.53 | Long term (current) use of anticoagulants |
| CDW | observation | observation_source_concept_id  | 2414345 | 205000000 | 1040755 | 0.51 | Postoperative follow-up visit, normally included in the surgical package, to indicate that an evaluation and management service was performed during a postoperative period for a reason(s) related to the original procedure |
| CDW | observation | observation_source_concept_id  | 2414393 | 205000000 | 903519 | 0.44 | Office or other outpatient visit for the evaluation and management of a new patient, which requires a medically appropriate history and/or examination and moderate level of medical decision making. When using total time on the date of the encounter for... |
| CDW | observation | value_as_concept_id  | 42709996 | 205000000 | 884034 | 0.43 | Smokes tobacco daily |
| CDW | observation | observation_source_concept_id  | 2414392 | 205000000 | 736461 | 0.36 | Office or other outpatient visit for the evaluation and management of a new patient, which requires a medically appropriate history and/or examination and low level of medical decision making. When using total time on the date of the encounter for code... |
| CDW | observation | observation_source_concept_id  | 2514399 | 205000000 | 731104 | 0.36 | Office or other outpatient visit for the evaluation and management of an established patient, which requires a medically appropriate history and/or examination and high level of medical decision making. When using total time on the date of the encounte... |
| CDW | observation | observation_source_concept_id  | 2414396 | 205000000 | 718197 | 0.35 | Office or other outpatient visit for the evaluation and management of an established patient, which requires a medically appropriate history and/or examination and straightforward medical decision making. When using total time on the date of the encoun... |
| CDW | observation | value_as_concept_id  | 4069297 | 205000000 | 521408 | 0.25 | Divorced |
| CDW | observation | value_as_concept_id  | 4143188 | 205000000 | 436958 | 0.21 | Widowed |
| CDW | observation | observation_type_concept_id  | 581413 | 205000000 | 262828 | 0.13 | Observation from Measurement |
| CDW | person | ethnicity_source_concept_id  |  | 2971731 | 2971731 | 100 |  |
| CDW | person | race_source_concept_id  |  | 2971731 | 2971731 | 100 |  |
| CDW | person | gender_source_concept_id  |  | 2971731 | 2971731 | 100 |  |
| CDW | person | gender_concept_id  | 8532 | 2971731 | 1692563 | 56.96 | FEMALE |
| CDW | person | ethnicity_concept_id  | 38003564 | 2971731 | 1689952 | 56.87 | Not Hispanic or Latino |
| CDW | person | gender_concept_id  | 8507 | 2971731 | 1276793 | 42.96 | MALE |
| CDW | person | ethnicity_concept_id  | 0 | 2971731 | 1188432 | 39.99 | No matching concept |
| CDW | person | race_concept_id  | 8527 | 2971731 | 1155280 | 38.88 | White |
| CDW | person | race_concept_id  | 0 | 2971731 | 865546 | 29.13 | No matching concept |
| CDW | person | race_concept_id  | 8516 | 2971731 | 845579 | 28.45 | Black or African American |
| CDW | person | ethnicity_concept_id  | 38003563 | 2971731 | 93347 | 3.14 | Hispanic or Latino |
| CDW | person | race_concept_id  | 8515 | 2971731 | 89437 | 3.01 | Asian |
| CDW | person | race_concept_id  | 8657 | 2971731 | 8165 | 0.27 | American Indian or Alaska Native |
| CDW | person | race_concept_id  | 8557 | 2971731 | 7724 | 0.26 | Native Hawaiian or Other Pacific Islander |
| CDW | person | gender_concept_id  | 0 | 2971731 | 2375 | 0.08 | No matching concept |
| CDW | procedure_occurrence | modifier_concept_id  |  | 41868731 | 41868731 | 100 |  |
| CDW | procedure_occurrence | procedure_type_concept_id  | 44786630 | 41868731 | 28713807 | 68.58 | Primary Procedure |
| CDW | procedure_occurrence | procedure_type_concept_id  | 42865906 | 41868731 | 11180331 | 26.7 | Condition Procedure |
| CDW | procedure_occurrence | procedure_concept_id  | 4036803 | 41868731 | 2356868 | 5.63 | General examination of patient |
| CDW | procedure_occurrence | procedure_source_concept_id  | 2514409 | 41868731 | 2006738 | 4.79 | Subsequent hospital inpatient or observation care, per day, for the evaluation and management of a patient, which requires a medically appropriate history and/or examination and high level of medical decision making. When using total time on the date o... |
| CDW | procedure_occurrence | procedure_concept_id  | 2514409 | 41868731 | 2006738 | 4.79 | Subsequent hospital inpatient or observation care, per day, for the evaluation and management of a patient, which requires a medically appropriate history and/or examination and high level of medical decision making. When using total time on the date o... |
| CDW | procedure_occurrence | procedure_type_concept_id  | 44786631 | 41868731 | 1974593 | 4.72 | Secondary Procedure |
| CDW | procedure_occurrence | procedure_source_concept_id  | 45552054 | 41868731 | 1653407 | 3.95 | Encounter for general adult medical examination without abnormal findings |
| CDW | procedure_occurrence | procedure_source_concept_id  | 2514408 | 41868731 | 1342543 | 3.21 | Subsequent hospital inpatient or observation care, per day, for the evaluation and management of a patient, which requires a medically appropriate history and/or examination and moderate level of medical decision making. When using total time on the da... |
| CDW | procedure_occurrence | procedure_concept_id  | 2514408 | 41868731 | 1342543 | 3.21 | Subsequent hospital inpatient or observation care, per day, for the evaluation and management of a patient, which requires a medically appropriate history and/or examination and moderate level of medical decision making. When using total time on the da... |
| CDW | procedure_occurrence | procedure_source_concept_id  | 2313816 | 41868731 | 1083534 | 2.59 | Electrocardiogram, routine ECG with at least 12 leads; interpretation and report only |
| CDW | procedure_occurrence | procedure_concept_id  | 2313816 | 41868731 | 1083534 | 2.59 | Electrocardiogram, routine ECG with at least 12 leads; interpretation and report only |
| CDW | procedure_occurrence | procedure_source_concept_id  | 44828573 | 41868731 | 912430 | 2.18 | Long-term (current) use of other medications |
| CDW | procedure_occurrence | procedure_concept_id  | 4141759 | 41868731 | 912430 | 2.18 | Long-term drug therapy |
| CDW | procedure_occurrence | procedure_source_concept_id  | 35225097 | 41868731 | 909718 | 2.17 | Encounter for immunization |
| CDW | procedure_occurrence | procedure_concept_id  | 4132855 | 41868731 | 909718 | 2.17 | Active or passive immunization |
| CDW | procedure_occurrence | procedure_source_concept_id  | 2313814 | 41868731 | 905102 | 2.16 | Electrocardiogram, routine ECG with at least 12 leads; with interpretation and report |
| CDW | procedure_occurrence | procedure_concept_id  | 2313814 | 41868731 | 905102 | 2.16 | Electrocardiogram, routine ECG with at least 12 leads; with interpretation and report |
| CDW | procedure_occurrence | procedure_source_concept_id  | 2514441 | 41868731 | 736465 | 1.76 | Critical care, evaluation and management of the critically ill or critically injured patient; first 30-74 minutes |
| CDW | procedure_occurrence | procedure_concept_id  | 2514441 | 41868731 | 736465 | 1.76 | Critical care, evaluation and management of the critically ill or critically injured patient; first 30-74 minutes |
| CDW | procedure_occurrence | procedure_source_concept_id  | 44826243 | 41868731 | 615030 | 1.47 | Routine general medical examination at a health care facility |
| CDW | procedure_occurrence | procedure_source_concept_id  | 2211359 | 41868731 | 582214 | 1.39 | Radiologic examination, chest; single view, frontal (Deprecated) |
| CDW | procedure_occurrence | procedure_concept_id  | 36713195 | 41868731 | 582214 | 1.39 | Plain X-ray of chest, anteroposterior view |
| CDW | procedure_occurrence | procedure_concept_id  | 4077697 | 41868731 | 571117 | 1.36 | Screening mammography |
| CDW | provider | specialty_source_concept_id  |  | 325513 | 325513 | 100 |  |
| CDW | provider | gender_concept_id  |  | 325513 | 325513 | 100 |  |
| CDW | provider | gender_source_concept_id  |  | 325513 | 325513 | 100 |  |
| CDW | provider | specialty_concept_id  | 0 | 325513 | 315211 | 96.84 | No matching concept |
| CDW | provider | specialty_concept_id  | 38004450 | 325513 | 1021 | 0.31 | Anesthesiology |
| CDW | provider | specialty_concept_id  | 903278 | 325513 | 616 | 0.19 | Hospital Medicine |
| CDW | provider | specialty_concept_id  | 38004451 | 325513 | 613 | 0.19 | Cardiology |
| CDW | provider | specialty_concept_id  | 38004456 | 325513 | 510 | 0.16 | Internal Medicine |
| CDW | provider | specialty_concept_id  | 38004675 | 325513 | 497 | 0.15 | Physician / Diagnostic Radiology |
| CDW | provider | specialty_concept_id  | 38004461 | 325513 | 489 | 0.15 | Obstetrics / Gynecology |
| CDW | provider | specialty_concept_id  | 38004465 | 325513 | 484 | 0.15 | Orthopedic Surgery |
| CDW | provider | specialty_concept_id  | 38004510 | 325513 | 473 | 0.15 | Emergency Medicine |
| CDW | provider | specialty_concept_id  | 38004447 | 325513 | 423 | 0.13 | General Surgery |
| CDW | visit_detail | visit_detail_concept_id  | 9201 | 27454991 | 27454991 | 100 | Inpatient Visit |
| CDW | visit_detail | visit_detail_type_concept_id  | 32035 | 27454991 | 27454991 | 100 | Visit derived from EHR encounter record |
| CDW | visit_detail | admitted_from_concept_id  |  | 27454991 | 27454991 | 100 |  |
| CDW | visit_detail | visit_detail_source_concept_id  |  | 27454991 | 27454991 | 100 |  |
| EPIC | care_site | place_of_service_concept_id  | 0 | 163 | 163 | 100 | No matching concept |
| EPIC | condition_occurrence | condition_status_concept_id  | 32896 | 33436825 | 27721603 | 82.91 | Discharge diagnosis |
| EPIC | condition_occurrence | condition_type_concept_id  | 32817 | 33436825 | 17337840 | 51.85 | EHR |
| EPIC | condition_occurrence | condition_type_concept_id  | 32019 | 33436825 | 10383763 | 31.05 | EHR billing diagnosis |
| EPIC | condition_occurrence | condition_type_concept_id  | 32840 | 33436825 | 5715222 | 17.09 | EHR problem list |
| EPIC | condition_occurrence | condition_status_concept_id  |  | 33436825 | 5118121 | 15.31 |  |
| EPIC | condition_occurrence | condition_source_concept_id  | 35207668 | 33436825 | 1671162 | 5 | Essential (primary) hypertension |
| EPIC | condition_occurrence | condition_concept_id  | 320128 | 33436825 | 1671162 | 5 | Essential hypertension |
| EPIC | condition_occurrence | condition_status_concept_id  | 32906 | 33436825 | 597101 | 1.79 | Resolved condition |
| EPIC | condition_occurrence | condition_concept_id  | 432867 | 33436825 | 535774 | 1.6 | Hyperlipidemia |
| EPIC | condition_occurrence | condition_source_concept_id  | 35207062 | 33436825 | 513900 | 1.54 | Mixed hyperlipidemia |
| EPIC | condition_occurrence | condition_concept_id  | 438720 | 33436825 | 513900 | 1.54 | Mixed hyperlipidemia |
| EPIC | condition_occurrence | condition_concept_id  | 201826 | 33436825 | 485272 | 1.45 | Type 2 diabetes mellitus |
| EPIC | condition_occurrence | condition_source_concept_id  | 35207065 | 33436825 | 481455 | 1.44 | Hyperlipidemia, unspecified |
| EPIC | condition_occurrence | condition_source_concept_id  | 35206882 | 33436825 | 481412 | 1.44 | Type 2 diabetes mellitus without complications |
| EPIC | condition_occurrence | condition_concept_id  | 4193704 | 33436825 | 481412 | 1.44 | Type 2 diabetes mellitus without complication |
| EPIC | condition_occurrence | condition_source_concept_id  | 35208190 | 33436825 | 357431 | 1.07 | Gastro-esophageal reflux disease without esophagitis |
| EPIC | condition_occurrence | condition_concept_id  | 4144111 | 33436825 | 357431 | 1.07 | Gastroesophageal reflux disease without esophagitis |
| EPIC | condition_occurrence | condition_source_concept_id  | 45586572 | 33436825 | 326945 | 0.98 | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| EPIC | condition_occurrence | condition_concept_id  | 764123 | 33436825 | 326945 | 0.98 | Atherosclerosis of coronary artery without angina pectoris |
| EPIC | condition_occurrence | condition_concept_id  | 433736 | 33436825 | 290119 | 0.87 | Obesity |
| EPIC | condition_occurrence | condition_source_concept_id  | 45542912 | 33436825 | 284750 | 0.85 | Other chronic pain |
| EPIC | condition_occurrence | condition_concept_id  | 436096 | 33436825 | 284750 | 0.85 | Chronic pain |
| EPIC | condition_occurrence | condition_concept_id  | 442077 | 33436825 | 261154 | 0.78 | Anxiety disorder |
| EPIC | condition_occurrence | condition_source_concept_id  | 35206992 | 33436825 | 256539 | 0.77 | Vitamin D deficiency, unspecified |
| EPIC | condition_occurrence | condition_source_concept_id  | 45605405 | 33436825 | 253968 | 0.76 | Type 2 diabetes mellitus with hyperglycemia |
| EPIC | condition_occurrence | condition_source_concept_id  | 35207173 | 33436825 | 226210 | 0.68 | Anxiety disorder, unspecified |
| EPIC | drug_exposure | route_concept_id  | 0 | 13162088 | 13162088 | 100 | No matching concept |
| EPIC | drug_exposure | drug_type_concept_id  | 32817 | 13162088 | 13162088 | 100 | EHR |
| EPIC | drug_exposure | drug_source_concept_id  | 1537215 | 13162088 | 516370 | 3.92 | propofol lipid emulsion |
| EPIC | drug_exposure | drug_concept_id  | 753626 | 13162088 | 516370 | 3.92 | propofol |
| EPIC | drug_exposure | drug_source_concept_id  | 46275280 | 13162088 | 360926 | 2.74 | 50 ML magnesium sulfate 40 MG/ML Injection |
| EPIC | drug_exposure | drug_concept_id  | 46275280 | 13162088 | 360926 | 2.74 | 50 ML magnesium sulfate 40 MG/ML Injection |
| EPIC | drug_exposure | drug_source_concept_id  | 19052492 | 13162088 | 356787 | 2.71 | phenylephrine tannate |
| EPIC | drug_exposure | drug_concept_id  | 1135766 | 13162088 | 356787 | 2.71 | phenylephrine |
| EPIC | drug_exposure | drug_source_concept_id  | 46274317 | 13162088 | 249106 | 1.89 | lidocaine hydrochloride anhydrous |
| EPIC | drug_exposure | drug_concept_id  | 989878 | 13162088 | 249112 | 1.89 | lidocaine |
| EPIC | drug_exposure | drug_source_concept_id  | 19080985 | 13162088 | 241058 | 1.83 | iohexol |
| EPIC | drug_exposure | drug_concept_id  | 19080985 | 13162088 | 241058 | 1.83 | iohexol |
| EPIC | drug_exposure | drug_source_concept_id  | 44784902 | 13162088 | 230060 | 1.75 | potassium chloride 20 MEQ Extended Release Oral Tablet [K-Tab] |
| EPIC | drug_exposure | drug_concept_id  | 44784902 | 13162088 | 230060 | 1.75 | potassium chloride 20 MEQ Extended Release Oral Tablet [K-Tab] |
| EPIC | drug_exposure | drug_source_concept_id  | 42707668 | 13162088 | 222642 | 1.69 | acetaminophen 325 MG Oral Tablet [Ringl] |
| EPIC | drug_exposure | drug_concept_id  | 42707668 | 13162088 | 222642 | 1.69 | acetaminophen 325 MG Oral Tablet [Ringl] |
| EPIC | drug_exposure | drug_source_concept_id  | 19082873 | 13162088 | 220490 | 1.68 | rocuronium bromide |
| EPIC | drug_exposure | drug_concept_id  | 19003953 | 13162088 | 220490 | 1.68 | rocuronium |
| EPIC | drug_exposure | drug_source_concept_id  | 40221382 | 13162088 | 172028 | 1.31 | sodium chloride 9 MG/ML Injection |
| EPIC | drug_exposure | drug_concept_id  | 40221382 | 13162088 | 172028 | 1.31 | sodium chloride 9 MG/ML Injection |
| EPIC | drug_exposure | drug_source_concept_id  | 19026684 | 13162088 | 169771 | 1.29 | ondansetron hydrochloride |
| EPIC | drug_exposure | drug_concept_id  | 1000560 | 13162088 | 169773 | 1.29 | ondansetron |
| EPIC | location | country_concept_id  | -99 | 5031082 | 5031082 | 100 |  |
| EPIC | measurement | meas_event_field_concept_id  |  | 130000000 | 130000000 | 100 |  |
| EPIC | measurement | unit_source_concept_id  |  | 130000000 | 130000000 | 100 |  |
| EPIC | measurement | measurement_type_concept_id  | 32817 | 130000000 | 130000000 | 100 | EHR |
| EPIC | measurement | unit_concept_id  | 0 | 130000000 | 130000000 | 100 | No matching concept |
| EPIC | measurement | value_as_concept_id  | 0 | 130000000 | 130000000 | 100 | No matching concept |
| EPIC | measurement | operator_concept_id  | 4172703 | 130000000 | 87507618 | 67.56 | = |
| EPIC | measurement | operator_concept_id  |  | 130000000 | 40624484 | 31.37 |  |
| EPIC | measurement | measurement_concept_id  | 3000483 | 130000000 | 3691268 | 2.85 | Glucose [Mass/volume] in Blood |
| EPIC | measurement | measurement_source_concept_id  | 3000483 | 130000000 | 3691268 | 2.85 | Glucose [Mass/volume] in Blood |
| EPIC | measurement | measurement_concept_id  | 3023103 | 130000000 | 3151373 | 2.43 | Potassium [Moles/volume] in Serum or Plasma |
| EPIC | measurement | measurement_source_concept_id  | 3023103 | 130000000 | 3151373 | 2.43 | Potassium [Moles/volume] in Serum or Plasma |
| EPIC | measurement | measurement_concept_id  | 3019550 | 130000000 | 3104215 | 2.4 | Sodium [Moles/volume] in Serum or Plasma |
| EPIC | measurement | measurement_source_concept_id  | 3019550 | 130000000 | 3104215 | 2.4 | Sodium [Moles/volume] in Serum or Plasma |
| EPIC | measurement | measurement_concept_id  | 3006906 | 130000000 | 3053426 | 2.36 | Calcium [Mass/volume] in Serum or Plasma |
| EPIC | measurement | measurement_concept_id  | 3004501 | 130000000 | 3053073 | 2.36 | Glucose [Mass/volume] in Serum or Plasma |
| EPIC | measurement | measurement_source_concept_id  | 3006906 | 130000000 | 3053426 | 2.36 | Calcium [Mass/volume] in Serum or Plasma |
| EPIC | measurement | measurement_source_concept_id  | 3004501 | 130000000 | 3053073 | 2.36 | Glucose [Mass/volume] in Serum or Plasma |
| EPIC | measurement | measurement_concept_id  | 3008295 | 130000000 | 3022633 | 2.33 | Osmolality of Serum or Plasma |
| EPIC | measurement | measurement_concept_id  | 3045716 | 130000000 | 3013324 | 2.33 | Anion gap in Serum or Plasma |
| EPIC | measurement | measurement_source_concept_id  | 3008295 | 130000000 | 3022633 | 2.33 | Osmolality of Serum or Plasma |
| EPIC | measurement | measurement_source_concept_id  | 3045716 | 130000000 | 3013324 | 2.33 | Anion gap in Serum or Plasma |
| EPIC | measurement | measurement_concept_id  | 3000963 | 130000000 | 2977029 | 2.3 | Hemoglobin [Mass/volume] in Blood |
| EPIC | measurement | measurement_source_concept_id  | 3000963 | 130000000 | 2977029 | 2.3 | Hemoglobin [Mass/volume] in Blood |
| EPIC | measurement | measurement_concept_id  | 3024929 | 130000000 | 2878119 | 2.22 | Platelets [#/volume] in Blood by Automated count |
| EPIC | measurement | measurement_source_concept_id  | 3024929 | 130000000 | 2878119 | 2.22 | Platelets [#/volume] in Blood by Automated count |
| EPIC | measurement | measurement_concept_id  | 3023314 | 130000000 | 2856472 | 2.21 | Hematocrit [Volume Fraction] of Blood by Automated count |
| EPIC | measurement | measurement_source_concept_id  | 3023314 | 130000000 | 2856472 | 2.21 | Hematocrit [Volume Fraction] of Blood by Automated count |
| EPIC | measurement | operator_concept_id  | 4171756 | 130000000 | 1175575 | 0.91 | < |
| EPIC | measurement | operator_concept_id  | 4171755 | 130000000 | 113034 | 0.09 | >= |
| EPIC | measurement | operator_concept_id  | 4172704 | 130000000 | 100605 | 0.08 | > |
| EPIC | measurement | operator_concept_id  | 4171754 | 130000000 | 182 | 0 | <= |
| EPIC | observation | obs_event_field_concept_id  |  | 2350000000 | 2350000000 | 100 |  |
| EPIC | observation | qualifier_concept_id  | -99 | 2350000000 | 2350000000 | 100 |  |
| EPIC | observation | unit_concept_id  | -99 | 2350000000 | 2350000000 | 100 |  |
| EPIC | observation | observation_type_concept_id  | 32817 | 2350000000 | 2350000000 | 100 | EHR |
| EPIC | observation | observation_source_concept_id  | 0 | 2350000000 | 2350000000 | 99.88 | No matching concept |
| EPIC | observation | observation_concept_id  | 0 | 2350000000 | 2350000000 | 99.86 | No matching concept |
| EPIC | observation | value_as_concept_id  | 0 | 2350000000 | 2350000000 | 99.86 | No matching concept |
| EPIC | observation | observation_concept_id  | 1340204 | 2350000000 | 723312 | 0.03 | History of event |
| EPIC | observation | value_as_concept_id  | 1340204 | 2350000000 | 723312 | 0.03 | History of event |
| EPIC | observation | observation_concept_id  | 439224 | 2350000000 | 379703 | 0.02 | Allergy to drug |
| EPIC | observation | value_as_concept_id  | -99 | 2350000000 | 493070 | 0.02 |  |
| EPIC | observation | observation_concept_id  | 46272450 | 2350000000 | 352123 | 0.01 | Long-term current use of drug therapy |
| EPIC | observation | observation_concept_id  | 46273937 | 2350000000 | 151149 | 0.01 | Long-term current use of anticoagulant |
| EPIC | observation | observation_concept_id  | 46272451 | 2350000000 | 128905 | 0.01 | Long-term current use of insulin |
| EPIC | observation | observation_source_concept_id  | 45537679 | 2350000000 | 317787 | 0.01 | Other long term (current) drug therapy |
| EPIC | observation | observation_source_concept_id  | 45552108 | 2350000000 | 151149 | 0.01 | Long term (current) use of anticoagulants |
| EPIC | observation | observation_source_concept_id  | 45576185 | 2350000000 | 128905 | 0.01 | Long term (current) use of insulin |
| EPIC | observation | value_as_concept_id  | 46272450 | 2350000000 | 352123 | 0.01 | Long-term current use of drug therapy |
| EPIC | observation | value_as_concept_id  | 46273937 | 2350000000 | 151149 | 0.01 | Long-term current use of anticoagulant |
| EPIC | observation | value_as_concept_id  | 46272451 | 2350000000 | 128905 | 0.01 | Long-term current use of insulin |
| EPIC | observation | observation_concept_id  | 438485 | 2350000000 | 113578 | 0 | Postoperative state |
| EPIC | observation | observation_concept_id  | 43530807 | 2350000000 | 105773 | 0 | Allergic disposition |
| EPIC | observation | observation_concept_id  | 4203722 | 2350000000 | 96518 | 0 | Patient encounter procedure |
| EPIC | observation | observation_concept_id  | 4060985 | 2350000000 | 79243 | 0 | Body mass index 30+ - obesity |
| EPIC | observation | observation_source_concept_id  | 37202304 | 2350000000 | 113578 | 0 | Other specified postprocedural states |
| EPIC | observation | observation_source_concept_id  | 45534458 | 2350000000 | 78993 | 0 | Other fatigue |
| EPIC | observation | observation_source_concept_id  | 35225415 | 2350000000 | 49342 | 0 | Presence of prosthetic heart valve |
| EPIC | observation | observation_source_concept_id  | 45585857 | 2350000000 | 45887 | 0 | Asymptomatic menopausal state |
| EPIC | observation | observation_source_concept_id  | 35225421 | 2350000000 | 44918 | 0 | Presence of intraocular lens |
| EPIC | observation | observation_source_concept_id  | 45581072 | 2350000000 | 43592 | 0 | Persons encountering health services in other specified circumstances |
| EPIC | observation | value_as_concept_id  | 438485 | 2350000000 | 113578 | 0 | Postoperative state |
| EPIC | observation | value_as_concept_id  | 4203722 | 2350000000 | 96518 | 0 | Patient encounter procedure |
| EPIC | observation | value_as_concept_id  | 4060985 | 2350000000 | 79243 | 0 | Body mass index 30+ - obesity |
| EPIC | observation | value_as_concept_id  | 4223659 | 2350000000 | 78993 | 0 | Fatigue |
| EPIC | person | gender_source_concept_id  | -99 | 6258439 | 6258439 | 100 |  |
| EPIC | person | ethnicity_source_concept_id  | -99 | 6258439 | 6258439 | 100 |  |
| EPIC | person | gender_concept_id  | 0 | 6258439 | 6258439 | 100 | No matching concept |
| EPIC | person | race_source_concept_id  | -99 | 6258439 | 6258439 | 100 |  |
| EPIC | person | ethnicity_concept_id  | 0 | 6258439 | 6258439 | 100 | No matching concept |
| EPIC | person | race_concept_id  | 0 | 6258439 | 6258439 | 100 | No matching concept |
| EPIC | procedure_occurrence | procedure_type_concept_id  | 32817 | 9686783 | 9686783 | 100 | EHR |
| EPIC | procedure_occurrence | modifier_concept_id  | 0 | 9686783 | 9469003 | 97.75 | No matching concept |
| EPIC | procedure_occurrence | procedure_source_concept_id  | 725068 | 9686783 | 591503 | 6.11 | Radiologic examination, chest; single view |
| EPIC | procedure_occurrence | procedure_concept_id  | 725068 | 9686783 | 591503 | 6.11 | Radiologic examination, chest; single view |
| EPIC | procedure_occurrence | procedure_source_concept_id  | 2313816 | 9686783 | 569189 | 5.88 | Electrocardiogram, routine ECG with at least 12 leads; interpretation and report only |
| EPIC | procedure_occurrence | procedure_concept_id  | 2313816 | 9686783 | 569189 | 5.88 | Electrocardiogram, routine ECG with at least 12 leads; interpretation and report only |
| EPIC | procedure_occurrence | procedure_source_concept_id  | 2313814 | 9686783 | 567102 | 5.85 | Electrocardiogram, routine ECG with at least 12 leads; with interpretation and report |
| EPIC | procedure_occurrence | procedure_concept_id  | 2313814 | 9686783 | 567102 | 5.85 | Electrocardiogram, routine ECG with at least 12 leads; with interpretation and report |
| EPIC | procedure_occurrence | procedure_source_concept_id  | 725069 | 9686783 | 319513 | 3.3 | Radiologic examination, chest; 2 views |
| EPIC | procedure_occurrence | procedure_concept_id  | 725069 | 9686783 | 319513 | 3.3 | Radiologic examination, chest; 2 views |
| EPIC | procedure_occurrence | procedure_source_concept_id  | 42627987 | 9686783 | 244849 | 2.53 | Screening mammography, bilateral (2-view study of each breast), including computer-aided detection (CAD) when performed |
| EPIC | procedure_occurrence | procedure_concept_id  | 42627987 | 9686783 | 244849 | 2.53 | Screening mammography, bilateral (2-view study of each breast), including computer-aided detection (CAD) when performed |
| EPIC | procedure_occurrence | procedure_source_concept_id  | 2211327 | 9686783 | 233181 | 2.41 | Computed tomography, head or brain; without contrast material |
| EPIC | procedure_occurrence | procedure_concept_id  | 2211327 | 9686783 | 233181 | 2.41 | Computed tomography, head or brain; without contrast material |
| EPIC | procedure_occurrence | modifier_concept_id  | -99 | 9686783 | 217780 | 2.25 |  |
| EPIC | procedure_occurrence | procedure_source_concept_id  | 46257421 | 9686783 | 200287 | 2.07 | Screening digital breast tomosynthesis, bilateral (List separately in addition to code for primary procedure) |
| EPIC | procedure_occurrence | procedure_concept_id  | 46257421 | 9686783 | 200287 | 2.07 | Screening digital breast tomosynthesis, bilateral (List separately in addition to code for primary procedure) |
| EPIC | procedure_occurrence | procedure_source_concept_id  | 724944 | 9686783 | 114064 | 1.18 | Radiologic examination, abdomen; 1 view |
| EPIC | procedure_occurrence | procedure_concept_id  | 724944 | 9686783 | 114064 | 1.18 | Radiologic examination, abdomen; 1 view |
| EPIC | procedure_occurrence | procedure_source_concept_id  | 2211378 | 9686783 | 111217 | 1.15 | Computed tomography, thorax, diagnostic; without contrast material |
| EPIC | procedure_occurrence | procedure_concept_id  | 2211378 | 9686783 | 111217 | 1.15 | Computed tomography, thorax, diagnostic; without contrast material |
| EPIC | procedure_occurrence | procedure_source_concept_id  | 2211381 | 9686783 | 87410 | 0.9 | Computed tomographic angiography, chest (noncoronary), with contrast material(s), including noncontrast images, if performed, and image postprocessing |
| EPIC | procedure_occurrence | procedure_concept_id  | 2211381 | 9686783 | 87410 | 0.9 | Computed tomographic angiography, chest (noncoronary), with contrast material(s), including noncontrast images, if performed, and image postprocessing |
| EPIC | provider | specialty_source_concept_id  | -99 | 77536 | 77536 | 100 |  |
| EPIC | provider | gender_concept_id  | -99 | 77536 | 77536 | 100 |  |
| EPIC | provider | gender_source_concept_id  | -99 | 77536 | 77536 | 100 |  |
| EPIC | provider | specialty_concept_id  | 0 | 77536 | 45079 | 58.14 | No matching concept |
| EPIC | provider | specialty_concept_id  | 38004456 | 77536 | 6271 | 8.09 | Internal Medicine |
| EPIC | provider | specialty_concept_id  | 38003851 | 77536 | 4633 | 5.98 | Family Medicine |
| EPIC | provider | specialty_concept_id  | 38004510 | 77536 | 2723 | 3.51 | Emergency Medicine |
| EPIC | provider | specialty_concept_id  | 38004451 | 77536 | 1957 | 2.52 | Cardiology |
| EPIC | provider | specialty_concept_id  | 38004447 | 77536 | 1942 | 2.5 | General Surgery |
| EPIC | provider | specialty_concept_id  | 45756825 | 77536 | 1833 | 2.36 | Radiology |
| EPIC | provider | specialty_concept_id  | 38004450 | 77536 | 1320 | 1.7 | Anesthesiology |
| EPIC | provider | specialty_concept_id  | 38003905 | 77536 | 919 | 1.19 | Obstetrics |
| EPIC | provider | specialty_concept_id  | 38004490 | 77536 | 879 | 1.13 | Physical Therapist |
| EPIC | visit_detail | visit_detail_source_concept_id  |  | 4329193 | 4329193 | 100 |  |
| EPIC | visit_detail | visit_detail_concept_id  | 0 | 4329193 | 4329193 | 100 | No matching concept |
| EPIC | visit_detail | admitted_from_concept_id  | 0 | 4329193 | 4329193 | 100 | No matching concept |
| EPIC | visit_detail | visit_detail_type_concept_id  | 44818518 | 4329193 | 4329193 | 100 | Visit derived from EHR record |