import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Визначення вхідних та вихідної змінних
title = ctrl.Antecedent(np.arange(0, 11, 1), 'title_similarity')
author_first_name = ctrl.Antecedent(
    np.arange(0, 11, 1), 'author_first_name_similarity')
author_last_name = ctrl.Antecedent(
    np.arange(0, 11, 1), 'author_last_name_similarity')
similarity_score = ctrl.Consequent(np.arange(0, 101, 1), 'similarity_score')

# Визначення нечітких множин та їх функцій належності
title['low'] = fuzz.trimf(title.universe, [0, 0, 5])
title['medium'] = fuzz.trimf(title.universe, [0, 5, 10])
title['high'] = fuzz.trimf(title.universe, [5, 10, 10])

author_first_name['low'] = fuzz.trimf(author_first_name.universe, [0, 0, 5])
author_first_name['medium'] = fuzz.trimf(
    author_first_name.universe, [0, 5, 10])
author_first_name['high'] = fuzz.trimf(author_first_name.universe, [5, 10, 10])

author_last_name['low'] = fuzz.trimf(author_last_name.universe, [0, 0, 5])
author_last_name['medium'] = fuzz.trimf(author_last_name.universe, [0, 5, 10])
author_last_name['high'] = fuzz.trimf(author_last_name.universe, [5, 10, 10])

similarity_score['low'] = fuzz.trimf(similarity_score.universe, [0, 0, 50])
similarity_score['medium'] = fuzz.trimf(
    similarity_score.universe, [25, 50, 75])
similarity_score['high'] = fuzz.trimf(
    similarity_score.universe, [50, 100, 100])

# Визначення правил нечіткої логіки
rule1 = ctrl.Rule(title['high'] | (author_first_name['high']
                  & author_last_name['medium']), similarity_score['high'])
rule2 = ctrl.Rule((title['medium'] & author_first_name['medium']) | (
    title['medium'] & author_last_name['medium']), similarity_score['medium'])
rule3 = ctrl.Rule(title['low'] | (author_first_name['low']
                  & author_last_name['low']), similarity_score['low'])

# Система контролю
similarity_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
similarity_sim = ctrl.ControlSystemSimulation(similarity_ctrl)

# Введення значень для вхідних змінних
similarity_sim.input['title_similarity'] = 8
similarity_sim.input['author_first_name_similarity'] = 6
similarity_sim.input['author_last_name_similarity'] = 3

# Виконання розрахунку
similarity_sim.compute()

# Виведення результату
print(f"Оцінка схожості: {similarity_sim.output['similarity_score']}")
