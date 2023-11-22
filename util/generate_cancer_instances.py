#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generates random instances for the cancers.owl onotlogy"""

import pandas as pds
import numpy as np
import random
import click
from textwrap import dedent

sexes = [
    "male", 
    "female"
]

cancers = [
    "uterine_corpus_cancer", 
    "cervical_cancer", 
    "fallopian_tube_adenocarcinoma", 
    "fallopian_tube_carcinoma", 
    "fallopian_tube_sarcoma",
    "testicular_sarcoma", 
    "testicular_lymphoma", 
    "testicular_leukemia", 
    "castration_sensitive_prostate_cancer", 
    "castration_resistant_prostate_cancer"
]

female_cancers = [
    "uterine_corpus_cancer", 
    "cervical_cancer", 
    "fallopian_tube_adenocarcinoma", 
    "fallopian_tube_carcinoma", 
    "fallopian_tube_sarcoma"
]

male_cancers = [
    "testicular_sarcoma", 
    "testicular_lymphoma", 
    "testicular_leukemia", 
    "castration_sensitive_prostate_cancer", 
    "castration_resistant_prostate_cancer"
]

comorbidities = [
    "asthma", 
    "lupus", 
    "hypertension", 
    "type_2_diabetes", 
    "type_1_diabetes"
]

social_habits = [
    "heaver_drinker", 
    "non-drinker", 
    "social_drinker", 
    "non-smoker", 
    "smoker"
]

sex_dict = {
    0: "male", 
    1: "female"
}

cancer_dict = {
    0: "uterine_corpus_cancer", 
    1: "cervical_cancer", 
    2: "fallopian_tube_adenocarcinoma", 
    3: "fallopian_tube_carcinoma", 
    4: "fallopian_tube_sarcoma",
    5: "testicular_sarcoma", 
    6: "testicular_lymphoma", 
    7: "testicular_leukemia", 
    8: "castration_sensitive_prostate_cancer", 
    9: "castration_resistant_prostate_cancer"
}

female_cancer_dict = {
    0: "uterine_corpus_cancer", 
    1: "cervical_cancer", 
    2: "fallopian_tube_adenocarcinoma", 
    3: "fallopian_tube_carcinoma", 
    4: "fallopian_tube_sarcoma"
}

male_cancer_dict = {
    0: "testicular_sarcoma", 
    1: "testicular_lymphoma", 
    2: "testicular_leukemia", 
    3: "castration_sensitive_prostate_cancer", 
    4: "castration_resistant_prostate_cancer"
}

comorbidity_dict = {
    0: "asthma", 
    1: "lupus", 
    2: "hypertension", 
    3: "type_2_diabetes", 
    4: "type_1_diabetes"
}

social_habit_dict = {
    0: "heaver_drinker", 
    1: "non-drinker", 
    2: "social_drinker", 
    3: "non-smoker", 
    4: "smoker"
}

def make_test_df(
        num,
        female_ratio=[0.5, 0.5],
        comorbidity_ratio=[0.2, 0.2, 0.2, 0.2, 0.2],
        social_habit_ratio=[0.2, 0.2, 0.2, 0.2, 0.2],
        female_cancer_ratio=[0.2, 0.2, 0.2, 0.2, 0.2],
        male_cancer_ratio=[0.2, 0.2, 0.2, 0.2, 0.2],
        cancer_ratio=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
        by_sex=True
    ):
    # create datafame with num rows
    # column headers are the ontology relations
    indexes = list(range(0, int(num)))
    cols = ["patient", "has_sex", "has_comorbidity", "has_social", "has_cancer"]
    df = pds.DataFrame(columns=cols, index=indexes)
    # print(range(0, len(sex_dict)))

    # generate a random arrays
    patients = np.random.choice(range(0, len(sex_dict)), num, p=female_ratio)
    comorbidities = np.random.choice(range(0, len(comorbidity_dict)), num, p=comorbidity_ratio)
    social_habits = np.random.choice(range(0, len(social_habit_dict)), num, p=social_habit_ratio)

    if by_sex:
        female_cancers = np.random.choice(range(0, len(female_cancer_dict)), num, p=female_cancer_ratio)
        male_cancers = np.random.choice(range(0, len(male_cancer_dict)), num, p=male_cancer_ratio)
    else:
        cancers = np.random.choice(range(0, len(cancer_dict)), num, p=cancer_ratio)
    
    for i in df.index:
        
        sex = sex_dict[patients[i]]
        comorbity = comorbidity_dict[comorbidities[i]]
        social_habit = social_habit_dict[social_habits[i]]

        if by_sex:
            cancer = (
                female_cancer_dict[female_cancers[i]] 
                if sex == 'female' 
                else male_cancer_dict[male_cancers[i]]
            )
        else:
            cancer = cancer_dict[cancers[i]]

        new_row = {
            "patient": f'patient_{i}',
            "has_sex": f'{sex}_{i}',
            "has_comorbidity": f'{comorbity}_{i}',
            "has_social": f'{social_habit}_{i}',
            "has_cancer": f'{cancer}_{i}'
        }
        
        print(new_row)
        # add new row
        df.loc[i] = new_row
    
    return df


def make_df(num):
    # create datafame with num rows
    # column headers are the ontology relations
    indexes = list(range(1, int(num) + 1))
    cols = ["patient", "has_sex", "has_cancer", "has_comorbidity", "has_social"]
    df = pds.DataFrame(columns=cols, index=indexes)
    
    # populate dataframe: rows will be translated to instances
    for i in df.index:
        # determine how many random instances to generate
        # random.randint returns a random number between 0 and X
        sexes_index = random.randint(0, len(sexes) - 1)
        comorbidities_index = random.randint(0,len(comorbidities) - 1)
        social_habits_index = random.randint(0, len(social_habits) - 1)
        cancers_index = random.randint(0, len(male_cancers) - 1)

        sex = sexes[sexes_index]
        cancer = male_cancers[cancers_index] if sex == "male" else female_cancers[cancers_index]
        comorbity = comorbidities[comorbidities_index]
        social_habit = social_habits[social_habits_index]

        new_row = {
            "patient": f'patient_{i}',
            "has_sex": f'{sex}_{i}',
            "has_comorbidity": f'{comorbity}_{i}',
            "has_social": f'{social_habit}_{i}',
            "has_cancer": f'{cancer}_{i}'
        }
        
        # df = pds.concat([df, pds.DataFrame(new_row)])
        df.loc[i] = new_row

    return df


def print_ttl(df, default_iri="http://example.com/cancers.owl/"):
    def instance(idv):
        cls = idv.rsplit("_", 1)[0] # get class name from indiviual
        return f':{idv} a :{cls} .'
    
    def triple(idv1, property, idv2):
        return f':{idv1} {property} :{idv2} .'
    
    print(
        dedent(f"""\
                @prefix : <{default_iri}> .
                @prefix owl: <http://www.w3.org/2002/07/owl#> .
                @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> ."""), "\n"
    )

    print("<http://example.com/cancer_instances.owl> a owl:Ontology .", "\n")

    print(
        dedent("""\
            :has_sex rdf:type owl:ObjectProperty .
            :has_comorbidity rdf:type owl:ObjectProperty .
            :has_social_habit rdf:type owl:ObjectProperty .
            :has_cancer rdf:type owl:ObjectProperty ."""), "\n"
    )

    for idx, patient, sex, comorbidity, social_habit, cancer in df.itertuples():
        # instantiate
        print(instance(patient))
        print(instance(sex))
        print(instance(cancer))
        print(instance(comorbidity))
        print(instance(social_habit))
        
        # relate instances
        print(triple(patient, ":has_sex", sex))
        print(triple(patient, ":has_comorbidity", comorbidity))
        print(triple(patient, ":has_social_habit", social_habit))
        print(triple(patient, ":has_cancer", cancer), '\n')


@click.command
@click.option('--num', default=50)
@click.option('--default_iri', default="http://example.com/cancers.owl/")
@click.option('--female_ratio', default="0.5, 0.5")
@click.option('--comorbidity_ratio', default="0.2, 0.2, 0.2, 0.2, 0.2")
@click.option('--social_habit_ratio', default="0.2, 0.2, 0.2, 0.2, 0.2")
@click.option('--female_cancer_ratio', default="0.2, 0.2, 0.2, 0.2, 0.2")
@click.option('--male_cancer_ratio', default="0.2, 0.2, 0.2, 0.2, 0.2")
@click.option('--cancer_ratio', default="0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1")
        
@click.option('--by_sex', default=True)
def main(
    num, 
    default_iri,
    female_ratio,
    comorbidity_ratio,
    social_habit_ratio,
    female_cancer_ratio,
    male_cancer_ratio,
    cancer_ratio,
    by_sex
):
    female_ratio = [float(i) for i in female_ratio.split(",")]
    comorbidity_ratio = [float(i) for i in comorbidity_ratio.split(",")]
    social_habit_ratio = [float(i) for i in social_habit_ratio.split(",")]
    female_cancer_ratio = [float(i) for i in female_cancer_ratio.split(",")]
    male_cancer_ratio = [float(i) for i in male_cancer_ratio.split(",")]
    cancer_ratio = [float(i) for i in cancer_ratio.split(",")]
    
    # df = make_df(num)
    df = make_test_df(
        num, 
        female_ratio,
        comorbidity_ratio,
        social_habit_ratio,
        female_cancer_ratio,
        male_cancer_ratio,
        cancer_ratio,
        by_sex
    )
    print_ttl(df, default_iri)
    

if __name__ == "__main__":
    main()