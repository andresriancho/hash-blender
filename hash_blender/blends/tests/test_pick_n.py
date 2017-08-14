import unittest

from hash_blender.blends.pick_n import (apply_orders,
                                        apply_slices,
                                        apply_key_value,
                                        pick_n)


class TestApplyOrders(unittest.TestCase):
    def test_apply_orders_1(self):
        result = [x for x in apply_orders([1, 2, 3])]
        self.assertEqual(result, [(1, 2, 3),
                                  (1, 3, 2),
                                  (2, 1, 3),
                                  (2, 3, 1),
                                  (3, 1, 2),
                                  (3, 2, 1)])


class TestApplySlices(unittest.TestCase):
    def test_apply_slices_1(self):
        result = [x for x in apply_slices([1, 2, 3])]
        self.assertEqual(result, [(1,), (2,), (3,),
                                  (1, 2), (1, 3), (2, 3),
                                  (1, 2, 3)])


class TestApplyKeyValue(unittest.TestCase):
    def test_apply_key_value_1(self):
        result = [x for x in apply_key_value({'a': '1', 'b': '2'})]
        self.assertEqual(result, [['1', '2'],
                                  ['a=1', 'b=2'],
                                  ['a:1', 'b:2']])


class TestPickN(unittest.TestCase):
    def test_pick_n_1(self):
        result = [x for x in pick_n({'a': '1', 'b': '2'})]
        self.assertEqual(result, [('1',),
                                  ('2',),
                                  ('1', '2'),
                                  ('2',),
                                  ('1',),
                                  ('2', '1'),
                                  ('a=1',),
                                  ('b=2',),
                                  ('a=1', 'b=2'),
                                  ('b=2',),
                                  ('a=1',),
                                  ('b=2', 'a=1'),
                                  ('a:1',),
                                  ('b:2',),
                                  ('a:1', 'b:2'),
                                  ('b:2',),
                                  ('a:1',),
                                  ('b:2', 'a:1')])
