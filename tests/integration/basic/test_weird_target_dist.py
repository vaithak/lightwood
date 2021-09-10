import unittest
import pandas as pd
from sklearn.metrics import r2_score
from lightwood.api.types import ProblemDefinition


class TestBasic(unittest.TestCase):
    def test_0_unkown_cateogires_in_test(self):
        from lightwood.api.high_level import predictor_from_problem

        # The target will be cateogircal and there will be a bunch of values in all datasets (train/dev/validation) that were not present in the others
        df = pd.DataFrame({
            'target': [1 for _ in range(500)] + [f'{i}cat' for i in range(100)],
            'y': [i for i in range(600)]
        })
        target = 'target'

        predictor = predictor_from_problem(df, ProblemDefinition.from_dict({'target': target, 'time_aim': 200}))
        predictor.learn(df)
        predictions = predictor.predict(df)